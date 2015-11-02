


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    
    
    <title>geonode/importservice.py at master · GeoNode/geonode · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="GeoNode/geonode" name="twitter:title" /><meta content="geonode - GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data." name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/132843?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/132843?v=3&amp;s=400" property="og:image" /><meta content="GeoNode/geonode" property="og:title" /><meta content="https://github.com/GeoNode/geonode" property="og:url" /><meta content="geonode - GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data." property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
        <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="41700A58:63D8:6F836A0:55E9F502" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged Out">
      <meta class="js-ga-set" name="dimension4" content="Current repo nav">
    <meta name="is-dotcom" content="true">
        <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <!-- </textarea> --><!-- '"` --><meta content="authenticity_token" name="csrf-param" />
<meta content="ac82NYFYuub/8ktWNHPyG1MDcygVCTII8fwB4MPPih+kSkn9UgpRv+88NTWasTQMkhKh+5q5pMUzsOY4y19zNA==" name="csrf-token" />
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-760a949769f2883d6febd885c263b1f47c072484378029415608e3a1460a25c6.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2-6fc9757ad8954989b540bc53f3b89b7d842c67ee992a0279907be799acc65714.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="b6cd24348762175d1d2f8fbbbace39c8">

      
  <meta name="description" content="geonode - GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data.">
  <meta name="go-import" content="github.com/GeoNode/geonode git https://github.com/GeoNode/geonode.git">

  <meta content="132843" name="octolytics-dimension-user_id" /><meta content="GeoNode" name="octolytics-dimension-user_login" /><meta content="701765" name="octolytics-dimension-repository_id" /><meta content="GeoNode/geonode" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="701765" name="octolytics-dimension-repository_network_root_id" /><meta content="GeoNode/geonode" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/GeoNode/geonode/commits/master.atom" rel="alternate" title="Recent Commits to geonode:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



      
      <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="btn btn-primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="btn" href="/login?return_to=%2FGeoNode%2Fgeonode%2Fblob%2Fmaster%2Fgeonode%2Fservices%2Fmanagement%2Fcommands%2Fimportservice.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/GeoNode/geonode/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/GeoNode/geonode/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/pricing" data-ga-click="(Logged out) Header, go to pricing, text:pricing">Pricing</a>
          </li>
      </ul>

  </div>
</div>



    <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>


        <div itemscope itemtype="http://schema.org/WebPage">
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">

        <div class="clearfix">
          
<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2FGeoNode%2Fgeonode"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <span class="octicon octicon-eye"></span>
    Watch
  </a>
  <a class="social-count" href="/GeoNode/geonode/watchers">
    85
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2FGeoNode%2Fgeonode"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/GeoNode/geonode/stargazers">
      331
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2FGeoNode%2Fgeonode"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/GeoNode/geonode/network" class="social-count">
        306
      </a>
    </li>
</ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public ">
  <span class="mega-octicon octicon-repo"></span>
  <span class="author"><a href="/GeoNode" class="url fn" itemprop="url" rel="author"><span itemprop="title">GeoNode</span></a></span><!--
--><span class="path-divider">/</span><!--
--><strong><a href="/GeoNode/geonode" data-pjax="#js-repo-pjax-container">geonode</a></strong>

  <span class="page-context-loader">
    <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
  </span>

</h1>

        </div>
      </div>
    </div>

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline ">
        <div class="repository-sidebar clearfix">
          
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/GeoNode/geonode/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/GeoNode/geonode" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /GeoNode/geonode">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/GeoNode/geonode/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /GeoNode/geonode/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/GeoNode/geonode/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /GeoNode/geonode/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/GeoNode/geonode/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /GeoNode/geonode/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/GeoNode/geonode/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /GeoNode/geonode/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/GeoNode/geonode/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /GeoNode/geonode/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

            <div class="only-with-full-nav">
                
<div class="js-clone-url clone-url open"
  data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/GeoNode/geonode.git" readonly="readonly" aria-label="HTTPS clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/GeoNode/geonode" readonly="readonly" aria-label="Subversion checkout URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



  <div class="clone-options">You can clone with
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone" class="inline-form js-clone-selector-form " data-form-nonce="04bfe3171c037e7a17e12f66d1d32ea84e5d9770" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="NS83bA7XcoKlffbk6HsmJWbg4WK7AxRkZ2ABx2FS2842Y/VStGngMRlw47w6jJAHJ94CuS9xZeKxWpHkjd7Gmg==" /></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form> or <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone" class="inline-form js-clone-selector-form " data-form-nonce="04bfe3171c037e7a17e12f66d1d32ea84e5d9770" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="SbCimydRmUP47CZaHYPmMpuHTXGjEqPJRndFxzvyBOg0DQioKMXnL6QN7vwU1M5hvWGSwZZ9FcgWWQbNA0b09w==" /></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
    <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
      <span class="octicon octicon-question"></span>
    </a>
  </div>

              <a href="/GeoNode/geonode/archive/master.zip"
                 class="btn btn-sm sidebar-button"
                 aria-label="Download the contents of GeoNode/geonode as a zip file"
                 title="Download the contents of GeoNode/geonode as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div>
        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/GeoNode/geonode/blob/f7834bda0302f75f7242b4a631f7555a7a694a48/geonode/services/management/commands/importservice.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:63a2f62a8258afa2a7ccf3814419529b -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/GeoNode/geonode/blob/2.0.x/geonode/services/management/commands/importservice.py"
               data-name="2.0.x"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="2.0.x">
                2.0.x
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/GeoNode/geonode/blob/2258/geonode/services/management/commands/importservice.py"
               data-name="2258"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="2258">
                2258
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/GeoNode/geonode/blob/master/geonode/services/management/commands/importservice.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+dev20141024171719/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+dev20141024171719"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+dev20141024171719">debian/2.4.0+dev20141024171719</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta25/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta25"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta25">debian/2.4.0+beta25</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta24/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta24"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta24">debian/2.4.0+beta24</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta23/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta23"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta23">debian/2.4.0+beta23</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta22/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta22"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta22">debian/2.4.0+beta22</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta21/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta21"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta21">debian/2.4.0+beta21</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta20/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta20"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta20">debian/2.4.0+beta20</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta19/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta19"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta19">debian/2.4.0+beta19</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta18/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta18"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta18">debian/2.4.0+beta18</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta17/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta17"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta17">debian/2.4.0+beta17</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta16/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta16"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta16">debian/2.4.0+beta16</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta15/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta15"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta15">debian/2.4.0+beta15</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta14/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta14"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta14">debian/2.4.0+beta14</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta13/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta13">debian/2.4.0+beta13</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta12/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta12">debian/2.4.0+beta12</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta11/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta11">debian/2.4.0+beta11</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta10/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta10">debian/2.4.0+beta10</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta9/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta9">debian/2.4.0+beta9</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta8/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta8">debian/2.4.0+beta8</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta7/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta7">debian/2.4.0+beta7</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta6/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta6">debian/2.4.0+beta6</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta5/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta5">debian/2.4.0+beta5</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta4/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta4">debian/2.4.0+beta4</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta3/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta3">debian/2.4.0+beta3</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta2/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta2">debian/2.4.0+beta2</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+beta1/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+beta1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+beta1">debian/2.4.0+beta1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha38/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha38"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha38">debian/2.4.0+alpha38</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha37/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha37"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha37">debian/2.4.0+alpha37</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha36/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha36"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha36">debian/2.4.0+alpha36</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha35/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha35"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha35">debian/2.4.0+alpha35</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha34/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha34"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha34">debian/2.4.0+alpha34</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha33/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha33"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha33">debian/2.4.0+alpha33</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha32/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha32"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha32">debian/2.4.0+alpha32</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha31/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha31"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha31">debian/2.4.0+alpha31</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha30/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha30"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha30">debian/2.4.0+alpha30</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha29/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha29"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha29">debian/2.4.0+alpha29</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha28/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha28"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha28">debian/2.4.0+alpha28</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha27/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha27"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha27">debian/2.4.0+alpha27</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha26/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha26"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha26">debian/2.4.0+alpha26</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha25/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha25"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha25">debian/2.4.0+alpha25</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha24/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha24"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha24">debian/2.4.0+alpha24</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha23/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha23"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha23">debian/2.4.0+alpha23</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha22/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha22"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha22">debian/2.4.0+alpha22</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha21/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha21"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha21">debian/2.4.0+alpha21</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha20/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha20"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha20">debian/2.4.0+alpha20</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha19/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha19"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha19">debian/2.4.0+alpha19</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha18/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha18"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha18">debian/2.4.0+alpha18</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha17/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha17"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha17">debian/2.4.0+alpha17</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha16/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha16"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha16">debian/2.4.0+alpha16</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha15/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha15"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha15">debian/2.4.0+alpha15</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha14/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha14"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha14">debian/2.4.0+alpha14</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha13/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha13">debian/2.4.0+alpha13</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha12/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha12">debian/2.4.0+alpha12</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha11/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha11">debian/2.4.0+alpha11</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha10/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha10">debian/2.4.0+alpha10</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha9/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha9">debian/2.4.0+alpha9</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha8/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha8">debian/2.4.0+alpha8</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha7/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha7">debian/2.4.0+alpha7</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha6/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha6">debian/2.4.0+alpha6</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha5/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha5">debian/2.4.0+alpha5</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha4/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha4">debian/2.4.0+alpha4</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha3/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha3">debian/2.4.0+alpha3</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha2/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha2">debian/2.4.0+alpha2</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.4.0+alpha1/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.4.0+alpha1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.4.0+alpha1">debian/2.4.0+alpha1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0b54/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0b54"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0b54">debian/2.0b54</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.1+thefinal0/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.1+thefinal0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.1+thefinal0">debian/2.0.1+thefinal0</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal7/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal7">debian/2.0.0+thefinal7</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal6/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal6">debian/2.0.0+thefinal6</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal5/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal5">debian/2.0.0+thefinal5</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal4/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal4">debian/2.0.0+thefinal4</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal3/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal3">debian/2.0.0+thefinal3</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal2/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal2">debian/2.0.0+thefinal2</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal1/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal1">debian/2.0.0+thefinal1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+thefinal0/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+thefinal0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+thefinal0">debian/2.0.0+thefinal0</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc13/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc13"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc13">debian/2.0.0+rc13</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc12/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc12"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc12">debian/2.0.0+rc12</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc10/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc10">debian/2.0.0+rc10</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc8/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc8">debian/2.0.0+rc8</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc7/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc7">debian/2.0.0+rc7</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc6/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc6">debian/2.0.0+rc6</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc5/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc5">debian/2.0.0+rc5</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc4/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc4">debian/2.0.0+rc4</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc3/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc3">debian/2.0.0+rc3</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc2/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc2">debian/2.0.0+rc2</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+rc1/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+rc1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+rc1">debian/2.0.0+rc1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta64/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta64"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta64">debian/2.0.0+beta64</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta63/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta63"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta63">debian/2.0.0+beta63</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta62/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta62"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta62">debian/2.0.0+beta62</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta61/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta61"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta61">debian/2.0.0+beta61</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta60/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta60"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta60">debian/2.0.0+beta60</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta59/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta59"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta59">debian/2.0.0+beta59</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta58/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta58"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta58">debian/2.0.0+beta58</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta57/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta57"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta57">debian/2.0.0+beta57</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta56/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta56"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta56">debian/2.0.0+beta56</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta55/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta55"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta55">debian/2.0.0+beta55</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta54/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta54"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta54">debian/2.0.0+beta54</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta53/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta53"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta53">debian/2.0.0+beta53</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta52/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta52"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta52">debian/2.0.0+beta52</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta51/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta51"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta51">debian/2.0.0+beta51</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/GeoNode/geonode/tree/debian/2.0.0+beta50/geonode/services/management/commands/importservice.py"
                 data-name="debian/2.0.0+beta50"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="debian/2.0.0+beta50">debian/2.0.0+beta50</a>
            </div>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="btn-group right">
      <a href="/GeoNode/geonode/find/master"
            class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-nw"
            data-pjax
            data-hotkey="t"
            aria-label="Quickly jump between files">
        <span class="octicon octicon-list-unordered"></span>
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </div>

    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/GeoNode/geonode" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">geonode</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/GeoNode/geonode/tree/master/geonode" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">geonode</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/GeoNode/geonode/tree/master/geonode/services" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">services</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/GeoNode/geonode/tree/master/geonode/services/management" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">management</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/GeoNode/geonode/tree/master/geonode/services/management/commands" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">commands</span></a></span><span class="separator">/</span><strong class="final-path">importservice.py</strong>
    </div>
  </div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@mbertrand" class="avatar" height="24" src="https://avatars0.githubusercontent.com/u/187676?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/mbertrand" rel="contributor">mbertrand</a></span>
        <time datetime="2014-07-15T14:14:34Z" is="relative-time">Jul 15, 2014</time>
        <div class="commit-title">
            <a href="/GeoNode/geonode/commit/96db67100b2fdb8cc61504cc8ed7e326ebbcfb4b" class="message" data-pjax="true" title="Fixed PEP8 violations">Fixed PEP8 violations</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>2</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="simod" href="/GeoNode/geonode/commits/master/geonode/services/management/commands/importservice.py?author=simod"><img alt="@simod" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/779380?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mbertrand" href="/GeoNode/geonode/commits/master/geonode/services/management/commands/importservice.py?author=mbertrand"><img alt="@mbertrand" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/187676?v=3&amp;s=40" width="20" /> </a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@simod" height="24" src="https://avatars1.githubusercontent.com/u/779380?v=3&amp;s=48" width="24" />
            <a href="/simod">simod</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mbertrand" height="24" src="https://avatars0.githubusercontent.com/u/187676?v=3&amp;s=48" width="24" />
            <a href="/mbertrand">mbertrand</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/GeoNode/geonode/raw/master/geonode/services/management/commands/importservice.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/GeoNode/geonode/blame/master/geonode/services/management/commands/importservice.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/GeoNode/geonode/commits/master/geonode/services/management/commands/importservice.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>


          <button type="button" class="octicon-btn disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
            <span class="octicon octicon-pencil"></span>
          </button>

        <button type="button" class="octicon-btn octicon-btn-danger disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </button>
    </div>

    <div class="file-info">
        97 lines (84 sloc)
        <span class="file-info-divider"></span>
      4.156 kB
    </div>
  </div>
  

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> django.core.management.base <span class="pl-k">import</span> BaseCommand</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> optparse <span class="pl-k">import</span> make_option</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> geonode.services.models <span class="pl-k">import</span> Service</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> geonode.services.views <span class="pl-k">import</span> _register_cascaded_service, _register_indexed_service, \</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">    _register_harvested_service, _register_cascaded_layers, _register_indexed_layers</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> geonode.people.utils <span class="pl-k">import</span> get_valid_user</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Command</span>(<span class="pl-e">BaseCommand</span>):</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Import a remote map service into GeoNode<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">    option_list <span class="pl-k">=</span> BaseCommand.option_list <span class="pl-k">+</span> (</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">        make_option(<span class="pl-s"><span class="pl-pds">&#39;</span>-o<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--owner<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>owner<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Name of the user account which should own the imported layers<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">        make_option(<span class="pl-s"><span class="pl-pds">&#39;</span>-r<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--registerlayers<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>registerlayers<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Register all layers found in the service<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">        make_option(<span class="pl-s"><span class="pl-pds">&#39;</span>-u<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--username<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>username<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Username required to login to this service if any<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">        make_option(<span class="pl-s"><span class="pl-pds">&#39;</span>-p<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--password<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>password<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Username required to login to this service if any<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">        make_option(<span class="pl-s"><span class="pl-pds">&#39;</span>-s<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--security<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>security<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Security permissions JSON - who can view/edit<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    args <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>url name type method<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">handle</span>(<span class="pl-smi">self</span>, <span class="pl-smi">url</span>, <span class="pl-smi">name</span>, <span class="pl-smi">type</span>, <span class="pl-smi">method</span>, <span class="pl-smi">console</span><span class="pl-k">=</span>sys.stdout, **<span class="pl-smi">options</span>):</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        user <span class="pl-k">=</span> options.get(<span class="pl-s"><span class="pl-pds">&#39;</span>user<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        owner <span class="pl-k">=</span> get_valid_user(user)</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        register_layers <span class="pl-k">=</span> options.get(<span class="pl-s"><span class="pl-pds">&#39;</span>registerlayers<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">        username <span class="pl-k">=</span> options.get(<span class="pl-s"><span class="pl-pds">&#39;</span>username<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        password <span class="pl-k">=</span> options.get(<span class="pl-s"><span class="pl-pds">&#39;</span>password<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        perm_spec <span class="pl-k">=</span> options.get(<span class="pl-s"><span class="pl-pds">&#39;</span>permspec<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">        register_service <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># First Check if this service already exists based on the URL</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        base_url <span class="pl-k">=</span> url</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">            service <span class="pl-k">=</span> Service.objects.get(<span class="pl-smi">base_url</span><span class="pl-k">=</span>base_url)</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> Service.DoesNotExist:</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">            service <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> service <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>This is an existing Service<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">            register_service <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># Then Check that the name is Unique</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            service <span class="pl-k">=</span> Service.objects.get(<span class="pl-smi">name</span><span class="pl-k">=</span>name)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> Service.DoesNotExist:</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">            service <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> service <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>This is an existing service using this name.<span class="pl-cce">\n</span>Please specify a different name.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> register_service:</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> _register_cascaded_service(<span class="pl-c1">type</span>, url, name, username, password, <span class="pl-smi">owner</span><span class="pl-k">=</span>owner, <span class="pl-smi">verbosity</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> _register_indexed_service(<span class="pl-c1">type</span>, url, name, username, password, <span class="pl-smi">owner</span><span class="pl-k">=</span>owner, <span class="pl-smi">verbosity</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> _register_harvested_service(url, name, username, password, <span class="pl-smi">owner</span><span class="pl-k">=</span>owner, <span class="pl-smi">verbosity</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Not Implemented (Yet)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>L<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Local Services not configurable via API<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Invalid method<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">            json_response <span class="pl-k">=</span> json.loads(response.content)</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>id<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> json_response:</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Service created with id of <span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> json_response[<span class="pl-s"><span class="pl-pds">&quot;</span>id<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">                service <span class="pl-k">=</span> Service.objects.get(<span class="pl-smi">id</span><span class="pl-k">=</span>json_response[<span class="pl-s"><span class="pl-pds">&quot;</span>id<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Something went wrong: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> response.content</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> service.id</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> register_layers</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> service <span class="pl-k">and</span> register_layers:</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">            layers <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> layer <span class="pl-k">in</span> service.layer_set.all():</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">                layers.append(layer.typename)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> service.method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> _register_cascaded_layers(user, service, layers, perm_spec)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> service.method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> _register_indexed_layers(user, service, layers, perm_spec)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> service.method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Not Implemented (Yet)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> service.method <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>L<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Local Services not configurable via API<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Invalid Service Type<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> response.content</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>
  </div>



      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://github.com/pricing" data-ga-click="Footer, go to pricing, text:pricing">Pricing</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.05364s from github-fe133-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <span class="octicon octicon-x"></span>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-06e65f5639cc52d1aaada53115a54614b60fa90ab446a673e3e1818df167663b.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-ee4ac88329bd04835855a912ad24ec8d4d05dd40c4a271721d3c67827d1e0f75.js"></script>
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>

