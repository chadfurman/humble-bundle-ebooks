import pytest

@pytest.fixture
def example_library_page_response():
    return '''HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
Set-Cookie: hmb_source=navbar; Domain=.humblebundle.com; Max-Age=86400; Path=/; expires=Mon, 31-May-2021 00:35:40 GMT
Set-Cookie: _simpleauth_sess=eyJ1c2VyX2lkIjo1OTU5OTEyOTY5NjAxMDI0LCJpZCI6InRWZE9HVzE4RWMiLCJhdXRoX3RpbWUiOjE2MjIzMzQ4NTd9|1622334940|df67ad2f299afbcb0a51a378113772f75a66ecaf; Domain=.humblebundle.com; Max-Age=15552000; Path=/; expires=Fri, 26-Nov-2021 00:35:40 GMT; secure; HttpOnly
X-Cloud-Trace-Context: 550695d23dfe653efbebd8420cf5dccf
Vary: Accept-Encoding
Date: Sun, 30 May 2021 00:35:40 GMT
Server: Google Frontend
Content-Length: 40228
Expires: Sun, 30 May 2021 00:35:40 GMT

<!doctype html>

<html lang="en" class="">
  <head>
    <title>
Humble Bundle - chad@chadfurman.com
</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script>
      window.noZensmooth = true;
      window.pageData = {atTime: 1622334940 };
      window.humble = window.humble || {};
      window.humble.locale = "en";
      window.humble.timezone = "America/Los_Angeles";

      window.humble.ie11ScriptsToLoad = [
        "https://humblebundle-a.akamaihd.net/static/hashed/230b5ad34db2149203fc119b74fb96ba968bcef1.js",
        "https://humblebundle-a.akamaihd.net/static/hashed/ee47b95548c49132e7080413b0af49b6318fbb04.js",
        "https://humblebundle-a.akamaihd.net/static/hashed/95bcf58c86417455c695def01a0961d2623ff678.js",
        "https://humblebundle-a.akamaihd.net/static/hashed/77174c175993866b13940bcbcbbb078e0331142b.js",
        "https://humblebundle-a.akamaihd.net/static/hashed/f00402ff4c562abd341a500a5f4b0c1043f974a1.js",
        "https://humblebundle-a.akamaihd.net/static/hashed/c5b3c44cb77ebe3f6a35879673a9eaf7dee99d90.js",
      ];
    </script>
    <script id="main-js" data-dist_version="c9ed87a47d080e3663d596d7acf24ed2c605d66f" src="https://humblebundle-a.akamaihd.net/c9ed87a47d080e3663d596d7acf24ed2c605d66f/dist/main.min.js"></script>


  
  <meta name="application-name" content="Humble Bundle">
  <meta name="msapplication-TileImage" content="https://humblebundle-a.akamaihd.net/static/hashed/49bccd0f2050e5fcfc3c442b269d4ff47b038ed9.png">
  <meta name='medium' content='news' />
  <meta name="theme-color" content="hsl(221, 11.52%, 32.35%)">
  <meta property='og:site_name' content='Humble Bundle' />
  <meta property='og:type' content='website' />
  <meta property="fb:app_id" content="101146256651042" />
  <meta property="fb:profile_id" content="162315830478396" />
  <meta property="fb:pages" content="162315830478396"><meta name="yandex-verification" content="4c70c59be0ff7c44" />

<meta name="viewport" content="width=device-width, initial-scale=1">

  

<link rel="apple-touch-icon" sizes="144x144" href="https://humblebundle-a.akamaihd.net/static/hashed/03df0490a53d595fd930f9fff52038366d60a05d.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://humblebundle-a.akamaihd.net/static/hashed/4c8bbc6fc7b2b8a9fa21e895afe1157188e28bfb.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://humblebundle-a.akamaihd.net/static/hashed/46cf2ed85a0641bfdc052121786440c70da77d75.png">
<link rel="shortcut icon" href="https://humblebundle-a.akamaihd.net/static/hashed/47e474eed38083df699b7dfd8d29d575e3398f1e.ico">
  <link rel="search" type="application/opensearchdescription+xml" title="Humble Bundle Search" href="https://humblebundle-a.akamaihd.net/static/hashed/734237ad071b57a64f3b131b3f86fc7ed670e794.xml" />
  <link rel='alternate' type='application/rss+xml' title='Humble Mumble' href='http://blog.humblebundle.com/rss' />

  
 
<style>
    
      #flash {
    position:fixed;
    right: 30px;
    top:10px;
    background: #eee;
    opacity: .8;
    border-radius: 10px;
    color: black;
    padding:20px;
    min-width: 200px;
    max-width: 400px;
    text-align: center;
    z-index: 99999;
    box-shadow: 1px 1px 5px #000;
    display:none;
  }
html, body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: 'Sofia Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 14px;
  padding: 0;
}

// Localize.js uses the <var> tag to indicate certain special things. However,
// some browsers apply special CSS to the <var> tag which we don't want. This
// effectively removes any special CSS that the browser might apply to <var>.
var {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
</style>
  
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/759ef916d602bba50fd836ab5d5a9d4c7030f92a.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/969b073f98a4e900c291869d4dc6309e34bacc2c.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/07e33c1618a25c99f67c6dc18981718918783bcb.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/9d28dc481927a4c845709e6888217f29ce6d6e95.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/9abe088ca50175f1e3ada1bec0fcb867970ec995.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/6c656a6ccefeff002c55866dc46bf6a5a5d07bc3.css" />

<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/4b99824166e80a68dc5fe83921690a3dd8503c63.css" />
<link rel="stylesheet" href="https://humblebundle-a.akamaihd.net/static/hashed/de4264bd3985ef79912f95fa50bc74ca53529087.css" />
<style></style>

<script>
  window.models = window.models || {};


window.models.user_json = {"maxRewardAmount": 10, "needs_to_opt_in": false, "wishlist": [], "has_epic_account_id": false, "gog_account_id": null, "battlenet_tag": null, "remind_me_products": [], "has_steam_link": true, "has_battlenet_link": false, "has_admin_access": false, "terms_url": "", "payment_credentials": [], "hasSharedDiscount": null, "rewardsDiscountAmount": 0, "origin_username": null, "selectedCountry": "US", "selectedLatitude": "42.107038", "selectedCity": "west springfield", "created": "2017-02-18T23:43:24.120100", "rewardsCharityAmount": 10, "hasIncreasedRewards": false, "logout_url": "/logout?goto\u003d/", "selectedLongitude": "-72.620368", "rewardsWalletAmount": 0, "is_logged_in": true, "gog_username": null, "origin_is_linked": false, "email": "chad@chadfurman.com", "selectedRegion": "MA"};

window.models.userSubscriptionState = {"failedBillingMonths": 0, "creditsRemaining": 0, "contentEndDateAfterBillDate": "2021-06-01T17:00:00", "isPaused": false, "monthlyNewestOwnedContentMachineName": null, "willReceiveFutureMonths": false, "monthlyPurchasedAnyContent": false, "newestOwnedTier": null, "nextBilledPlan": "", "lastSkippedContentMachineName": null, "unpauseDt": "2021-06-01T17:00:00", "wasPaused": false, "billDate": "2021-06-29T17:00:00", "canResubscribe": false, "monthlyNewestOwnedContentEnd": null, "currentlySkippingContentMachineName": null, "monthlyOwnsAnyContent": false, "perksStatus": "inactive", "canBeConvertedFromGiftSubToPayingSub": false, "monthlyOwnsActiveContent": false, "monthlyNewestOwnedContentGamekey": null};
window.models.request = {
  country_code: "US",
  captcha_enabled: true,
  vat_rate: 0.0,
  is_mobile: false,
  isAndroidApp: false
};
</script>
    
      




<script>

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-467050-6', 'auto');
  ga('set', 'dimension4', "tVdOGW18Ec");
  ga('set', 'userId', "5959912969601024");
// dimension5 = 'Logged State' to differentiate logged in vs. logged out users
ga('set', 'dimension5', 'Logged In');

// TODO: Clean this up in ENG-22003
if (window.models.userSubscriptionState.perksStatus === 'active') {
  // dimension6 = 'Subscriber State' to differentiate subscribed users vs. not
  ga('set', 'dimension6', 'Subscribed');
} else {
  ga('set', 'dimension6', 'Not Subscribed');
}

ga('require', 'GTM-M5CXJM2');
  ga('require', 'displayfeatures');
  ga('require', 'ecommerce');
  ga('require', 'linkid', 'linkid.js');

  window._hbga = function(verb) {
    ga.apply(this, arguments);
  };





  var expiry = new Date();
  expiry.setTime(expiry.getTime() + 24*60*60*1000*7);  // 7 days in the future

_hbga('send', 'pageview', {
  'hitCallback': function () {
    if (window.gaData && window.gaData['UA-467050-6'] && window.gaData['UA-467050-6']['experiments']) {
      var expData = window.gaData['UA-467050-6']['experiments'];
      for (var experimentId in expData) {
        var experimentVariant = expData[experimentId];
        document.cookie = 'hmb_medium=goptimize_' + escape(experimentId) + ';path=/;expires=' + expiry.toUTCString();
        document.cookie = 'hmb_campaign=goptimize_' + escape(experimentVariant) + ';path=/;expires=' + expiry.toUTCString();
      }
      if (window.internalUIEventBus) {
        // Override panel is initialized first
        // You can trigger an event for experiment data
        window.internalUIEventBus.trigger('gaExperiments', expData);
      }
    }
  }
});




  window._gaTrackEvent = function(category, action, opt_label, opt_value, opts) {
    category = category || ('/' + window.location.pathname.split('/')[1]);
    _hbga('send', 'event', category, action, opt_label, opt_value, opts);
  };
  window._gaTrackPageview = function(page) {
    _hbga('send', 'pageview', page);
  };
  window._gaTrackEventNoninteractive = function(category, action, opt_label, opt_value) {
    _gaTrackEvent(category, action, opt_label, opt_value, {'nonInteraction': 1})
  };

</script>
<script>


(function() {
  // Load the heap library JS
  window.heap = window.heap || [], heap.load = function (e, t) {window.heap.appid = e, window.heap.config = t = t || {};var r = document.createElement("script");r.type = "text/javascript", r.async = !0, r.src = "https://cdn.heapanalytics.com/js/heap-" + e + ".js";var a = document.getElementsByTagName("script")[0];a.parentNode.insertBefore(r, a);for (var n = function (e) {return function () {heap.push([e].concat(Array.prototype.slice.call(arguments, 0)))}}, p = ["addEventProperties", "addUserProperties", "clearEventProperties", "identify", "resetIdentity", "removeEventProperty", "setEventProperties", "track", "unsetEventProperty"], o = 0; o < p.length; o++) heap[p[o]] = n(p[o])};

  // Initialize the heap object with our heap app ID
  heap.load('2199522758');
  var userJson = window.models.user_json;
  var subscriptionJson = window.models.userSubscriptionState;
  var userProperties = $.extend({}, subscriptionJson);
  userProperties.userCountry = userJson.selectedCountry || window.models.request.country_code;
  userProperties.locale = 'en';
  var userID = 'ahFzfmhyLWh1bWJsZWJ1bmRsZXIRCxIEVXNlchiAgMj7pZDLCgw';
  if (userID) {
    heap.identify(userID);
  }
  heap.addUserProperties(userProperties);
  var eventProperties = {
    'logged_in': userJson.is_logged_in,
    'subscription_perks_status': subscriptionJson.perksStatus,
    'pause_state': subscriptionJson.isPaused,
    'owns_active_content': subscriptionJson.monthlyOwnsActiveContent,
  };
  heap.addEventProperties(eventProperties);
})();
</script>

<script>
  if (!window.cj) window.cj = {};
  cj.sitePage = {"emailHash": "726bbe17f35f3113df5189f1a2d6e3497f8533c6b5c3f8d5be56fead849d80b0", "enterpriseId": 1563072, "userId": 5959912969601024, "pageType": "accountCenter"};
  (function(a,b,c,d){
    a='https://www.mczbf.com/tags/11509/tag.js';
    b=document;c='script';d=b.createElement(c);d.src=a;
    d.type='text/java'+c;d.async=true;
    d.id='cjapitag'
    ;a=b.getElementsByTagName(c)[0];a.parentNode.insertBefore(d,a)})();
</script>
<script>
    
  (function(){
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.src = 'https://www.googletagmanager.com/gtag/js?id=AW-752198208';
    head.insertBefore(script, head.firstChild);
  })();

  window.dataLayer = window.dataLayer || [];
  window.gtag = function(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-752198208');



  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window,document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1658430177760250');
  fbq('track', 'PageView');
  







  var tjPromise = $.getScript('https://www.tp88trk.com/scripts/sdk/everflow.js', function() {
    EF.click({
      offer_id: EF.urlParameter('oid'),
      affiliate_id: EF.urlParameter('affid'),
      sub1: EF.urlParameter('sub1'),
      sub2: EF.urlParameter('sub2'),
      sub3: EF.urlParameter('sub3'),
      sub4: EF.urlParameter('sub4'),
      sub5: EF.urlParameter('sub5'),
      uid: EF.urlParameter('uid'),
      transaction_id: EF.urlParameter('utm_term'),
    });
  });


  
  window.userPassedEvidonCheck = true;
</script>

    

<script></script>
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "WebSite",
    "url": "https://www.humblebundle.com/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://www.humblebundle.com/store/search?search={search_term}",
      "query-input": "required name=search_term"
    }
  }
</script>

  
<script src="https://ubistatic2-a.akamaihd.net/uplay-connect/v3/prod/default/sdk/connectSdkPublic.js" type="text/javascript"></script>



  
<link rel="alternate" hreflang="ru" href="https://ru.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="fr" href="https://fr.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="en" href="https://www.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="zh" href="https://zh.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="de" href="https://de.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="it" href="https://it.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="es" href="https://es.humblebundle.com/home/library" />
  
<link rel="alternate" hreflang="x-default" href="https://www.humblebundle.com/home/library" />

  </head>
  <body>

  <div class="page-wrap">
  
    
    <div id="page-top-messages"></div>

  
    <div id="site-xpromo-banner"
     class="banner js-banner small-banner top is-hidden"
     style="background-image: url('https://hb.imgix.net/a86fc016a6d0451241f47f742eb5ae7ad3c4178a.jpg?auto=compress,format&amp;fit=clip&amp;w=1920&amp;s=1a6582da8475a96fcc12ec884856dd80');">
  <div class="js-admin-edit"
     data-entity-kind="banner" 
    
     data-machine-name="210504_12for12_premium_banner" 
    >
  </div>
  <a class="page-banner-link js-page-banner-link"
     href="https://www.humblebundle.com/subscription?hmb_campaign=210504_12for12_premium_banner&amp;hmb_medium=banner"
     data-banner="210504_12for12_premium_banner">
  
    <p class="body"><b><h2>Get Metro Exodus PC Enhanced Edition for only $8!</h2></b></p>
  
  </a>
  
  <button href="#" class="dismiss-button js-dismiss-button" aria-label="Dismiss Banner"><i class="hb hb-times" aria-hidden="true"></i></button>
  </div>
  

  <div class="js-navigation-tracker"></div>  
<div class="navigation-container-v2 js-navigation-container-v2">
  <nav class="navbar js-navbar">
    <div class="navbar-content">

      
      <a class="navbar-item logo-navbar-item mobile" href="/?hmb_source=navbar">
        <img src="https://humblebundle-a.akamaihd.net/static/hashed/62dadb2abc89d033ab694400b601154e9c6ff292.svg" alt="Humble">  
      </a>

      <a class="navbar-item logo-navbar-item desktop" href="/?hmb_source=navbar">
        <img src="https://humblebundle-a.akamaihd.net/static/hashed/4814f84495cd679571cb94896978da3825562075.svg" alt="Humble">  
      </a>

      
      
<section class="tabs tabs-navbar-item js-tabs-navbar-item js-maintain-scrollbar-on-dropdown">
  
  <a class="navbar-item not-dropdown button-title" href="/bundles?hmb_source=navbar">
    <span class="navbar-icon-text-wrapper">
      <i class="navbar-item-icon hb hb-bindle mobile"></i>
      <span class="navbar-item-text">Bundles</span>
    </span>
  </a>
    
  <a class="navbar-item not-dropdown button-title
      "
      
    href="/subscription?hmb_source=navbar">
      
    <span class="navbar-icon-text-wrapper">
      
      <i class="navbar-item-icon hb hb-choice mobile"></i>
      <span class="navbar-item-text">Choice</span>
      
    </span>
  </a>
    
  <a class="navbar-item not-dropdown button-title
      "
      
    href="/store?hmb_source=navbar">
      
    <span class="navbar-icon-text-wrapper">
      
      <i class="navbar-item-icon hb hb-shopping-cart-full mobile"></i>
      <span class="navbar-item-text">Store</span>
      
    </span>
  </a>
    
  <div class="about-dropdown-container">
    <button class="no-style-button js-about-item-dropdown-toggle js-navbar-dropdown navbar-item navbar-item-dropdown dropdown-button button-title" data-dropdown-type="about-dropdown">
      <span class="navbar-icon-text-wrapper">
        <i class="navbar-item-icon hb hb-about mobile"></i>
        <span class="navbar-item-text">About</span>
        <i class="navbar-item-icon hb hb-caret-down desktop secondary-caret about-item-dropdown-caret" aria-hidden="true"></i>
      </span>
    </button>
  </div>
    
</section>


      
      
  <li class="navbar-item site-search js-site-search">
    <span class="js-site-minisearch site-minisearch-view">
        <span class="site-searchbar-holder js-navbar-dropdown js-search-item-dropdown-toggle" data-dropdown-type="search-dropdown">
        <div class="searchbar">
          <input id="site-search" aria-label="Search" class="site-search js-search" placeholder="Search"/>
          <button class="no-style-button clear-search-button js-clear-search-button" aria-label="Clear search">
            <i class="hb hb-search" aria-hidden="true"></i>
          </button>
        </div>
      </span>
      <div class="site-search-results-holder js-search-holder">
        <div class="site-search-message js-message"></div>
        <div class="site-search-results js-results js-disable-body-scroll"></div>
        <div class="site-search-navigation js-search-navigation">
          <button class="no-style-button page-navigation js-prev-page" aria-label="Previous set of search results">
            <i class="hb hb-angle-double-left hb-2x"></i>
          </button>
          <div class="site-search-information">
            <a class="site-search-link js-search-link"></a>
            <span class="site-search-paging js-search-paging"></span>
          </div>
          <button class="no-style-button page-navigation js-next-page" aria-label="Next set of search results">
            <i class="hb hb-angle-double-right hb-2x"></i>
          </button>
        </div>
      </div>
    </span>
  </li>


      
      

<button class="js-user-item-dropdown-toggle js-navbar-dropdown js-maintain-scrollbar-on-dropdown js-user-navbar-item navbar-item navbar-item-dropdown user-navbar-item logged-in button-title no-style-button" data-dropdown-type="user-dropdown" aria-label="Account Access" aria-live="polite">
  <span class="navbar-icon-text-wrapper">
    <i class="navbar-item-icon hb hb-user-circle-o " aria-hidden="true"></i>
    <i class="hb hb-caret-down desktop secondary-caret user-item-dropdown-caret" aria-hidden="true"></i>
    <span class="navbar-item-text mobile">Account</span>
  </span>
</button>


    </div>
  </nav>
  <nav class="bottom-navbar js-bottom-navbar">
      <div class="navbar-content"></div>
  </nav>
</div>
  <nav class="tabbar">
  </nav>
<div class="base-main-wrapper">
      <div class="page_title"></div>
      <div class="inner-main-wrapper">

<div class="js-library-holder js-holder is-hidden"></div>
<div class="js-purchase-holder js-holder is-hidden"></div>
<div class="js-claimed-orders-holder js-holder is-hidden"></div>
<div class="js-key-manager-holder js-holder is-hidden"></div>
<div class="js-coupon-holder js-holder is-hidden"></div>
<div class="bottom-tab-shortcuts">
  <a href="/home/library">Library</a> |
  <a href="/home/purchases">Purchases</a> |
  <a href="/home/keys">Keys &amp; Entitlements</a> |
  <a href="/home/coupons">Coupons</a>
</div>
</div>
  
</div>




<div class="grayout">
  <div class="grayout-inner">
  </div>
</div>

<script>
/* v1.0.1 */(function(b){b.fn.mailcheck=function(a,b){var d="yahoo.com,google.com,hotmail.com,gmail.com,me.com,aol.com,mac.com,live.com,comcast.net,googlemail.com,msn.com,hotmail.co.uk,yahoo.co.uk,facebook.com,verizon.net,sbcglobal.net,att.net,gmx.com,mail.com".split(",");if("object"===typeof a&&void 0===b)a.domains=a.domains||d;else{var e=a,a=b;a.domains=e||d}(d=Kicksend.mailcheck.suggest(encodeURI(this.val()),a.domains))?a.suggested&&a.suggested(this,d):a.empty&&a.empty(this)}})(jQuery);
var Kicksend={mailcheck:{threshold:3,suggest:function(b,a){var b=b.toLowerCase(),c=this.splitEmail(b),d=this.findClosestDomain(c.domain,a);return d?{address:c.address,domain:d,full:c.address+"@"+d}:!1},findClosestDomain:function(b,a){for(var c,d=99,e=null,f=0;f<a.length;f++){if(b===a[f])return!1;c=this.stringDistance(b,a[f]);c<d&&(d=c,e=a[f])}return d<=this.threshold&&null!==e?e:!1},stringDistance:function(b,a){if(null==b||0===b.length)return null==a||0===a.length?0:a.length;if(null==a||0===a.length)return b.length;
for(var c=0,d=0,e=0,f=0;c+d<b.length&&c+e<a.length;){if(b[c+d]==a[c+e])f++;else for(var g=e=d=0;5>g;g++){if(c+g<b.length&&b[c+g]==a[c]){d=g;break}if(c+g<a.length&&b[c]==a[c+g]){e=g;break}}c++}return(b.length+a.length)/2-f},splitEmail:function(b){b=b.split("@");if(2>b.length)return!1;for(var a=0;a<b.length;a++)if(""===b[a])return!1;return{domain:b.pop(),address:b.join("@")}}}};
</script>
<script>
window.modal_attributes = {
  request_reason: "",
  base_url_secure: "https://www.humblebundle.com",
  goto: null,
  qs: null,
  is_eu_country: false,
  is_in_china: false,
  isMobile: false,
  method: 'post'  // Force all modal forms to be post instead of the default get to avoid leaking sensitive information during form submit
};
</script>


<div id='flash'></div>
  <script>
    var _user_id = "HTo81re1lRak2UeQ38bFmlmYkAJJvvBPKCtquAyj2m6XOh1OQKiv55qxYTYwEX0COa";
var _session_id = "tVdOGW18Ec";

var _sift = _sift || [];
_sift.push(['_setAccount', '2bc56aa86f']);
_sift.push(['_setUserId', _user_id]);
_sift.push(['_setSessionId', _session_id]);
_sift.push(['_trackPageview']);
(function () {
  function ls() {
    var e = document.createElement('script');
    e.type = 'text/javascript';
    e.async = true;
    e.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdn.sift.com/s.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(e, s);
  }

  if (window.attachEvent) {
    window.attachEvent('onload', ls);
  } else {
    window.addEventListener('load', ls, false);
  }
})();
  </script>
  <script></script>

  <script>
    /*
 *	TypeWatch 2.0 - Original by Denny Ferrassoli / Refactored by Charles Christolini
 *
 *	Examples/Docs: www.dennydotnet.com
 *
 *  Copyright(c) 2007 Denny Ferrassoli - DennyDotNet.com
 *  Coprright(c) 2008 Charles Christolini - BinaryPie.com
 *
 *  Dual licensed under the MIT and GPL licenses:
 *  http://www.opensource.org/licenses/mit-license.php
 *  http://www.gnu.org/licenses/gpl.html
 */

(function(jQuery) {
  jQuery.fn.typeWatch = function(o) {
    // Options
    var options = jQuery.extend({
      wait : 750,
      callback : function() {
      },
      highlight : true,
      captureLength : 2
    }, o);

    function checkElement(timer, override) {
      var elTxt = jQuery(timer.el).val();

      // Fire if text > options.captureLength AND text != saved txt OR if override AND text > options.captureLength
      if ((elTxt.length > options.captureLength && elTxt.toUpperCase() != timer.text)
              || (override && elTxt.length > options.captureLength)) {
        timer.text = elTxt.toUpperCase();
        timer.cb(elTxt);
      }
    };

    function watchElement(elem) {
      // Must be text or textarea
      if (elem.type.toUpperCase() == "TEXT" || elem.nodeName.toUpperCase() == "TEXTAREA") {

        // Allocate timer element
        var timer = {
          timer : null,
          text : jQuery(elem).val().toUpperCase(),
          cb : options.callback,
          el : elem,
          wait : options.wait
        };

        // Set focus action (highlight)
        if (options.highlight) {
          jQuery(elem).focus(
                  function() {
                    this.select();
                  });
        }

        // Key watcher / clear and reset the timer
        var startWatch = function(evt) {
          var timerWait = timer.wait;
          var overrideBool = false;

          if (evt.keyCode == 13 && this.type.toUpperCase() == "TEXT") {
            timerWait = 1;
            overrideBool = true;
          }

          var timerCallbackFx = function() {
            checkElement(timer, overrideBool)
          }

          // Clear timer
          clearTimeout(timer.timer);
          timer.timer = setTimeout(timerCallbackFx, timerWait);

        };

        jQuery(elem).keydown(startWatch);
        // HTML5 adds an "input" event which is a more reliable way of telling
        // when the field has changed -- it fires for things like browser
        // autofill (where there is no keydown event). For browsers that support
        // it, we bind startWatch to fire here too.
        jQuery(elem).bind('input', startWatch);
      }
    }

    ;

    // Watch Each Element
    return this.each(function(index) {
      watchElement(this);
    });

  };

})(jQuery);
var MAILCHECK_DOMAINS = ['gmail.com', 'hotmail.com', 'yahoo.com', 'hotmail.co.uk', 'googlemail.com', 'gmx.de', 'live.com', 'live.ca', 'web.de', 'aol.com', 'msn.com', 'comcast.net', 'me.com', 'gmx.net', 'hotmail.fr', 'mail.ru', 'yahoo.co.uk', 'live.co.uk', 'yandex.ru', 'mac.com', 'yahoo.de', 'yahoo.fr'];




function isValidEmail(e) {
  return (e != '') && /.+@.+\..+/.test(e);
}

function live_email_check($field, setEmailMessage) {
  var emailValid = false;
  $field.mailcheck({
    domains: MAILCHECK_DOMAINS,
    suggested: function($input, suggestion) {
      // set the error text to the suggested correction
      var message = 'Did you mean <a href="#" class="suggested-email" data-email="' + suggestion['full'] + '">' + suggestion['address'] + '@<strong>' + suggestion['domain'] + '</strong></a>?'
      var $msgField = setEmailMessage($field, message);
      $msgField.find('.suggested-email').click(function(e) {
        e.preventDefault();
        $input.val($(this).data('email'));
        live_email_check($field, setEmailMessage, false);
      });
      emailValid = true;
    },
    empty: function($input) {
      // no suggested domain correction, check if the email address looks valid
      var email = $input.val();
      emailValid = isValidEmail(email);
      if (emailValid) {
        setEmailMessage($field, false);
      } else {
        setEmailMessage($field, 'Email address is not valid', true);
      }
    }
 });
  return emailValid;
}
// this method will set up email "validation" and error correction.
// Parameters:
//   $field is the input field to bind to
//   setEmailMessage is a function that takes the input field the error is related to and a message to set.
//     It sets the message then returns the error holder.
function bindEmailField($field, setEmailMessage){
  if (!window.humble || window.humble.locale !== 'en') {
    // only show email suggestion on EN locale as it only supports common EN email providers
    return;
  }
  function bound_live_email_check () {
    live_email_check($field, setEmailMessage);
  }
  $field.typeWatch({
    callback: bound_live_email_check,
    captureLength: -1,
    highlight: false,
    wait: 500
  });
}
var flash = $('#flash');

function show_flash(message){
  flash.text(message)
  flash.show();

  setTimeout(function() {
    flash.fadeOut();
  },5000);
}

function set_flash(message) {
  $.cookie('hbflash', message, {path: '/'});
}

$(function(){
  function show_flash(message){
    flash.text(message)
    flash.show();

    setTimeout(function() {
      flash.fadeOut();
    },5000);
  }

  var flashmessage = $.cookie('hbflash');
  if (flashmessage == 'None') {
    flashmessage = '';
  }

  if (flashmessage) {
    show_flash(flashmessage);
    $.cookie('hbflash', 'None', {path: '/'});
  }

  flash.click(function(){
    flash.fadeOut();
  });
});
// When CSS4 is widely-supported by all the modern browsers, detecting touch support may not be necessary depending on the usage of the touch.
$(function(){
  // Class assignment can be used for touch screen problems. Such as :hover.
  if ('ontouchstart' in window) {
    $('body').addClass('touch-support');
  }
});
  </script>

   
  </div>


  <footer class="site-footer">
  <div class="max-width-wrapper">
    <div class="footer-content">
      <div class="brand">
        <a href="/"><img src="https://humblebundle-a.akamaihd.net/static/hashed/4814f84495cd679571cb94896978da3825562075.svg" alt="Humble Bundle Logo"></a>
      </div>

      <div class="refer-container">
        <p class="refer-message">Get up to $15 Wallet Credit to spend on your next store purchase!</p>
        <a href="/refer?hmb_source=footer&hmb_medium=footer_refer&hmb_campaign=refer_a_friend" class="refer-link">Invite a Friend</a>
      </div>

      <section class="footer-links">
        <div class="footer-links-info">
          <h2>About</h2>
          <ul class="info-links-list">
            <li><a href="https://blog.humblebundle.com/en" target="_blank">Blog</a></li>
            <li><a href="https://support.humblebundle.com" target="_blank">Support</a></li>
            <li><a href="/resender" target="_blank">Order Resender</a></li>
            <li><a href="/developer" target="_blank">Developer</a></li>
          </ul>
        </div>
        <div class="footer-links-trending">
          <h2>Trending Games</h2>
          <ul class="trending-games-list">

            <li><a href="/store/biomutant" target="_blank">BIOMUTANT</a></li>

            <li><a href="/store/necromunda-hired-gun" target="_blank">Necromunda: Hired Gun</a></li>

            <li><a href="/store/mass-effect-legendary-edition" target="_blank">Mass Effect Legendary Edition</a></li>

            <li><a href="/store/grim-dawn" target="_blank">Grim Dawn</a></li>

            <li><a href="/store/wasteland-3" target="_blank">Wasteland 3</a></li>

            <li><a href="/store/mechwarrior-5-mercenaries" target="_blank">MechWarrior 5: Mercenaries</a></li>

            <li><a href="/store/grim-dawn-ashes-of-malmouth-expansion" target="_blank">Grim Dawn - Ashes of Malmouth Expansion</a></li>

            <li><a href="/store/grim-dawn-forgotten-gods-expansion" target="_blank">Grim Dawn - Forgotten Gods Expansion</a></li>

          </ul>
        </div>
      </section>
      <div class="social-and-language-container">

        <div class="language-dropdown-container">
          <button class="js-language-dropdown language-dropdown">
            <p><i class="hb hb-globe-fas"></i> Language: English</p> <i class="hb hb-caret-down"></i>
          </button>
          <div class="language-container js-language-container">
            <ul>
  
              <li class="">
                <button data-locale="ru" class="js-change-language no-style-button">Русский</button>
              </li>
  
              <li class="">
                <button data-locale="fr" class="js-change-language no-style-button">Français</button>
              </li>
  
              <li class=" active ">
                <button data-locale="en" class="js-change-language no-style-button">English</button>
              </li>
  
              <li class="">
                <button data-locale="zh_CN" class="js-change-language no-style-button">简体中文</button>
              </li>
  
              <li class="">
                <button data-locale="de" class="js-change-language no-style-button">Deutsch</button>
              </li>
  
              <li class="">
                <button data-locale="it" class="js-change-language no-style-button">Italiano</button>
              </li>
  
              <li class="">
                <button data-locale="es" class="js-change-language no-style-button">Español</button>
              </li>
  
            </ul>
          </div>
        </div>

        <div class="socialcontainer">



          <a href="https://www.facebook.com/humblebundle/" class="social-temp"><span class="sr-only">Facebook</span><i class="hb hb-facebook"></i></a>
          <a href="https://twitter.com/humble" class="social-temp"><span class="sr-only">Twitter</span><i class="hb hb-twitter"></i></a>
          <a href="https://www.instagram.com/humblebundle" class="social-temp"><span class="sr-only">Instagram</span><i class="hb hb-instagram"></i></a>

          <a href="https://blog.humblebundle.com/en" class="social-temp"><span class="sr-only">Blog</span><i class="hb hb-blog"></i></a>
        </div>
        <p class="humble-community-text">The Humble community has contributed over $197,000,000 to charity since 2010, making an amazing difference to causes all over the world.</p>
        <div class="legal-links">
          <ul class="legal-links-list first">
            <li><a href="/terms" target="_blank">Terms of Service</a></li>
            <li><a href="/privacy" target="_blank">Privacy Policy</a></li>
          </ul>
          <ul class="legal-links-list second">
            <li><a href="/cookie-policy" target="_blank">Cookie Policy</a></li>
            <li><a href="/legal" target="_blank">Legal Notices</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</footer>

<script id="base-webpack-json-data" type="application/json">
  {"banner": {
      "bannerToRender": null,
      "idToInit": null
    },"production": true,
    "countryCode": "US",
    "navbar": {
      "ipInChina": null,
      "BLOG_URL": "https://blog.humblebundle.com/en",
      "algoliaInfo": {
        "indexName": "slave_product_query_site_search",
        "publicKey": "AYSZEWDAZ2",
        "searchKey": "5229f8b3dec4b8ad265ad17ead42cb7f",
        "curtimeOverride": null
      },
      "searchOptions": {
        "pricing_constants": {
          "current_country": "US",
          "pricing_currency": "USD",
          "exchange_rates": {"USD": 1.0, "IDR": 14334.162411464338, "BGN": 1.6107725251194203, "ISK": 120.6555756876956, "ILS": 3.2516883544720803, "GBP": 0.7063498599901169, "DKK": 6.124691154669741, "CAD": 1.2115796409158293, "JPY": 110.07247570416736, "HUF": 286.4849283478834, "RON": 4.051721297973975, "MYR": 4.133503541426454, "SEK": 8.338823916982376, "SGD": 1.3261406687530886, "HKD": 7.7619831988140335, "AUD": 1.3009388898039862, "CHF": 0.9026519519024873, "KRW": 1116.669411958491, "CNY": 6.376379509141822, "TRY": 8.598089276890134, "HRK": 6.191731181024543, "NZD": 1.384533025860649, "THB": 31.299621149728218, "EUR": 0.8235875473562839, "NOK": 8.383297644539615, "RUB": 73.64544556086312, "INR": 72.54653269642563, "MXN": 20.028907922912207, "CZK": 20.961126667764784, "BRL": 5.258112337341459, "PLN": 3.695025531213968, "PHP": 47.82984681271619, "ZAR": 13.83174106407511}
        },
        "subscriptioncontent_icon": "https://humblebundle-a.akamaihd.net/static/hashed/74c9dedf4e02d66d912f6cd308562bd00a46d646.jpg",
        "bundle_icon": "https://humblebundle-a.akamaihd.net/static/hashed/cf3858ca434246e23c6474e37cd123028f9d1b98.svg"
      },
      "userDropdown": {
        "hasDashboard": false,
        "isPartner": false
      }
    }
  }
</script>

<script id="user-home-json-data" type="application/json">
  {"userOptions": {"maxRewardAmount": 10, "needs_to_opt_in": false, "wishlist": [], "has_epic_account_id": false, "gog_account_id": null, "battlenet_tag": null, "remind_me_products": [], "has_steam_link": true, "has_battlenet_link": false, "has_admin_access": false, "terms_url": "", "payment_credentials": [], "hasSharedDiscount": null, "rewardsDiscountAmount": 0, "origin_username": null, "selectedCountry": "US", "selectedLatitude": "42.107038", "selectedCity": "west springfield", "created|datetime": "2017-02-18T23:43:24.120100", "rewardsCharityAmount": 10, "hasIncreasedRewards": false, "logout_url": "/logout?goto\u003d/", "selectedLongitude": "-72.620368", "rewardsWalletAmount": 0, "is_logged_in": true, "gog_username": null, "origin_is_linked": false, "email": "chad@chadfurman.com", "selectedRegion": "MA"}, "showSingleSignOn": true, "hasAdmin": false, "csrfToken": {}, "gamekeys": ["2cut2AGkahN7WqBK", "2AZm2qDRvVUeqbKY", "2VnWY5u6C77Pc6yw"], "baseSubscriptionMsrp|money": {"currency": "USD", "amount": 200.0}, "user_max_reward_amount": 10, "activePlatform": "windows", "isEuCountry": false, "ipInChina": false, "baseSubscriptionPrice|money": {"currency": "USD", "amount": 19.99}, "exchangeRates": {"USD|decimal": 1.0, "IDR|decimal": 14334.162411464338, "BGN|decimal": 1.6107725251194203, "ISK|decimal": 120.6555756876956, "ILS|decimal": 3.2516883544720803, "GBP|decimal": 0.7063498599901169, "DKK|decimal": 6.124691154669741, "CAD|decimal": 1.2115796409158293, "JPY|decimal": 110.07247570416736, "HUF|decimal": 286.4849283478834, "RON|decimal": 4.051721297973975, "MYR|decimal": 4.133503541426454, "SEK|decimal": 8.338823916982376, "SGD|decimal": 1.3261406687530886, "HKD|decimal": 7.7619831988140335, "AUD|decimal": 1.3009388898039862, "CHF|decimal": 0.9026519519024873, "KRW|decimal": 1116.669411958491, "CNY|decimal": 6.376379509141822, "TRY|decimal": 8.598089276890134, "HRK|decimal": 6.191731181024543, "NZD|decimal": 1.384533025860649, "THB|decimal": 31.299621149728218, "EUR|decimal": 0.8235875473562839, "NOK|decimal": 8.383297644539615, "RUB|decimal": 73.64544556086312, "INR|decimal": 72.54653269642563, "MXN|decimal": 20.028907922912207, "CZK|decimal": 20.961126667764784, "BRL|decimal": 5.258112337341459, "PLN|decimal": 3.695025531213968, "PHP|decimal": 47.82984681271619, "ZAR|decimal": 13.83174106407511}, "csrfTokenInput": "\u003cinput type\u003d\u0027hidden\u0027 class\u003d\u0027csrftoken\u0027 name\u003d\u0027_le_csrf_token\u0027 value\u003d\u0027kWde3JVlKQv9sDKP-1-1622331956\u0027 /\u003e", "debug": false, "bannerOptions": null, "csrfFormKey": {}}
</script>


<script src="https://humblebundle-a.akamaihd.net/static/hashed/eefeb32f3f393456803fe1033963e0c2e20f3ad1.js"></script>
<script src="https://humblebundle-a.akamaihd.net/static/hashed/6f4bfd34a6a43a5540c5c20760537ccd499f4b4b.js"></script>

<div id="site-modal"></div>
  </body>
</html>
'''