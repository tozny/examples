# TozID OpenId Connect Implicit Flow Sample

This sample app demonstrates how to authenticate users in single page apps
and does not require any server side code.

The sample makes use of a pure [Javascript OpenId Connect Client](https://github.com/IdentityModel/oidc-client-js). We have included a minified
version of this client in `public/javascripts/oidc-client.min.js` or you can
fetch the [latest version here](https://github.com/IdentityModel/oidc-client-js/tree/dev/dist).

We have kept this sample to minimum functionality. However the UserManager in OIDC Client
library has many useful features for authenticating via popups, logging out, and
getting user info. Check out the [wiki](https://github.com/IdentityModel/oidc-client-js/wiki) and [samples](https://github.com/IdentityModel/oidc-client-js/tree/dev/sample/public) in the Github repo.

## Setup
In order to run this sample you need to setup a TozID realm using your Tozny developer account, along with creating an OpenId Connect (OIDC) client
application in the TozId Realm Admin portal of the created realm.

If you don't have a Tozny developer account [you can sign up here](https://www.dashboard.tozny.com/register).

Clone this repo and then update <b>/javascripts/main.js</b>  `TOZID_CLIENT_ID` variable with the <b>client_id</b> you obtained from TozID when setting up the OIDC application, along with the `TOZID_HOSTNAME` variable with the location of the TozID instance your client application is a part of (for most cases this will be `https://id.tozny.com`).

```js
const TOZID_CLIENT_ID = 'demo';
const TOZID_HOSTNAME = 'https://id.tozny.com';
```

Note that with the Implicit flow the **client_secret** is not required.

The sample will automatically set the **redirect_uri** to the host
location that the sample is running on. You need to make sure that
this matches what you specified as the Redirect Uri when you
setup your OIDC app connector in the TozId Realm Admin portal.

## Run
This sample uses node to serve up the single home page.

From the command line run
```bash
> npm install
> npm start
```

### Local testing
By default these samples will run on `http://localhost:3000`.

You will need to add your callback url (e.g. `http://localhost:3000`) to the list of approved **Redirect URIs** for your OIDC client application via the TozID Realm Admin portal the client application is located in.
