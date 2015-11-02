from django.core.management.base import BaseCommand,CommandError
from optparse import make_option
from owslib.wmts import WebMapTileService
from geonode.geoserver.helpers import set_attributes
from geonode.services.models import Service, Layer, ServiceLayer
import os,json,re,urlparse
import logging
import uuid
logger = logging.getLogger("importrumsey")

def process_wmts_service(url, name, type, username, password, wmts=None, owner=None, parent=None):
    """
    Create a new WMTS service
    """
    if wmts is None:
        wmts = WebMapTileService(url)
    try:
        base_url = _clean_url(
            wmts.getOperationByName('GetTile').methods['Get']['url'])

        if base_url and base_url != url:
            url = base_url
            wmts = WebMapTileService(base_url)
    except:
        logger.info(
            "Could not retrieve GetMap url, using originally supplied URL %s" % url)
        pass
    try:
        service = Service.objects.get(base_url=url)
        return_dict = [{'status': 'ok',
                        'msg': _("This is an existing service"),
                        'service_id': service.pk,
                        'service_name': service.name,
                        'service_title': service.title
                        }]
        return HttpResponse(json.dumps(return_dict),
                            mimetype='application/json',
                            status=200)
    except:
        pass
    title = wmts.identification.title
    if not name:
        if title:
            name = wmts.identification.title
        else:
            name = urlsplit(url).netloc
    for layer,layer_metadata in wmts.contents.items():
        if layer is None or layer_metadata.name is None:
            continue
        logger.info("Registering layer %s" % layer_metadata.name)
        layer_uuid = str(uuid.uuid1())
        try:
            keywords = map(lambda x: x[:100], layer_metadata.keywords)
        except:
            keywords = []
        if not layer_metadata.abstract:
            abstract = ""
        else:
            abstract = layer_metadata.abstract

        bbox = list(
            layer_metadata.boundingBoxWGS84 or (-179.0, -89.0, 179.0, 89.0))

        # Need to check if layer already exists??
        saved_layer, created = Layer.objects.get_or_create(
            typename=layer_metadata.name,
            service=service,
            defaults=dict(
                name=layer_metadata.name,
                store=service.name,  # ??
                storeType="remoteStore",
                workspace="remoteWorkspace",
                title=layer_metadata.title or layer_metadata.name,
                abstract= layer_metadata.abstract or ("Not provided"),
                uuid=layer_uuid,
                owner=None,
                srid=layer_metadata.tilematrixsets,
                bbox_x0=bbox[0],
                bbox_x1=bbox[2],
                bbox_y0=bbox[1],
                bbox_y1=bbox[3]
            )
        )
        if created:
            saved_layer.save()
            saved_layer.set_default_permissions()
            saved_layer.keywords.add(*keywords)
            set_attributes(saved_layer)

            service_layer, created = ServiceLayer.objects.get_or_create(
                typename=layer_metadata.name,
                service=service
            )
            service_layer.layer = saved_layer
            service_layer.title = layer_metadata.title
            service_layer.description = layer_metadata.abstract
            service_layer.styles = layer_metadata.styles
            service_layer.save()
    message = "%d Layers Registered" % count
    return_dict = {'status': 'ok', 'msg': message}
    return HttpResponse(json.dumps(return_dict),
                        mimetype='application/json',
                        status=200)
    

def process_layer(layer):
    #We process the david rumsey map collection and get the wmts endpoint as we can not register the layer without a service and as a remote service
    if layer['tps_tileserver']:
        url = urlparse.urlparse(layer['tps_tileserver'])
        wmts_params  = re.compile('map/(.*?)tps', re.DOTALL |  re.IGNORECASE).findall(url.path)
        wmts_params = str(wmts_params[0]) + 'wmts'
        wmts_endpoint = '/dbefee297985a052031f2710f30d811ecb583319/map/'+ wmts_params
        wmts_url = urlparse.urljoin("http://georeferencer.tileserver.com",wmts_endpoint)
        user = None
        password = None
        wmts = None
        owner = None
        process_wmts_service(wmts_url,layer['id'],'WMTS', user, password,wmts,owner)
    return layer
class Command(BaseCommand):
    help = 'Take the json entities dump from the David Rumsey maps collection and import them into GeoNode'
    args = 'file [file]'

    option_list = BaseCommand.option_list + (
        make_option(
            "-f", 
            "--file", 
            dest = "filename",
            help = "specify import file", 
            metavar = "FILE"
        ),)

    def handle(self, *args, **options):
        # make sure file option is present
        if options['filename'] == None :
            raise CommandError("Option `--file=...` must be specified.")

        # make sure file path resolves
        if not os.path.isfile(options['filename']) :
            raise CommandError("File does not exist at the specified path.")
        json_data=open(options['filename']).read()
        data = json.loads(json_data)
        for layer in data:
            process_layer(layer)
