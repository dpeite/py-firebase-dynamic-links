# Firebase Dynamic Links python client

Simple python client to generate [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/). It allows to 
use a custom domain and fields for generate links for android and ios.


### Requirements

* Python >= 3.4
* PIP
* API Key from [Firebase console Settings page](https://console.firebase.google.com/project/_/settings/general/).


### Installation
```bash
pip install py-firebase-dynamic-links
```

### Usage
```python
from firebase_dynamic_links import DynamicLinks

api_key = 'your_api_key'
domain = 'example.page.link'
timeout = 10
dl = DynamicLinks(api_key, domain, timeout) # or DynamicLinks(api_key, domain)
params = {
    "androidInfo": {
        "androidPackageName": 'packagename',
        "androidFallbackLink": 'fallbacklink',
        "androidMinPackageVersionCode": '1'
    },
}
# dl.generate_dynamic_link(url_to_redirect, create_short_url, params) or
# dl.generate_dynamic_link(url_to_redirect)
short_link = dl.generate_dynamic_link('http://google.es', True, params) #https://example.page.link/h77c
```
* `api_key`: [Key from firebase console](https://console.firebase.google.com/project/_/settings/general/)
* `domain`: Domain uri prefix created in firebase console. For example `example.page.link` or your custom domain.
* `timeout`: Timeout for the api call
* `params`: Dictionary of optional params. For example:
```python
{
    "androidInfo": {
      "androidPackageName": string,
      "androidFallbackLink": string,
      "androidMinPackageVersionCode": string
    },
    "iosInfo": {
      "iosBundleId": string,
      "iosFallbackLink": string,
      "iosCustomScheme": string,
      "iosIpadFallbackLink": string,
      "iosIpadBundleId": string,
      "iosAppStoreId": string
    }
}
```
[More params available here](https://firebase.google.com/docs/reference/dynamic-links/link-shortener)


### Reference
[https://firebase.google.com/docs/dynamic-links/rest](https://firebase.google.com/docs/dynamic-links/rest)  
[https://firebase.google.com/docs/reference/dynamic-links/link-shortener](https://firebase.google.com/docs/reference/dynamic-links/link-shortener)