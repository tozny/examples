# TozID OpenId Connect Implicit Flow Sample

This sample app demonstrates how to authenticate users in single page apps
and does not require any server side code.

The sample makes use of a pure [Javascript OpenId Connect Client](https://github.com/IdentityModel/oidc-client-js). We have included a minified
version of this client in `public/javascripts/oidc-client.min.js` or you can
fetch the [latest version here](https://github.com/IdentityModel/oidc-client-js/tree/dev/dist).

We have kept this sample to minimum functionality. However the UserManager in OIDC Client
library has many useful features for authenticating via popups, logging out, and
getting user info. Check out the [wiki](https://github.com/IdentityModel/oidc-client-js/wiki) and [samples](https://github.com/IdentityModel/oidc-client-js/tree/dev/sample/public) in the Github repo.

For a complete walkthrough of how to use this example app in combination with TozID to enable Single Sign On, read the [demo doc](./TozIDPoweredOIDCImplicitFlowThirdPartySSO).

This doc can be edited and re-exported as a PDF from [Google Drive](https://docs.google.com/document/d/1mQNwbp2_3g0UdxBziSV5rpbFERV2HXi_om27kDwlPw8/edit)

## Setup
This repo contains two ways to run the example. One runs it locally in a node server and a hardcoded configuration file. The other will build it with the configuration set from environment variables.

In order to run this sample you need to setup a TozID realm using your Tozny developer account, along with creating an OpenId Connect (OIDC) client
application in the TozId Realm Admin portal of the created realm.

If you don't have a Tozny developer account [you can sign up here](https://www.dashboard.tozny.com/register).

### Getting code

Clone this repo and run `npm install`.

### Configuring the application

This app requires you to configure a OIDC client application in TozID's realm admin dashboard. Follow this instructions [here](TozIDPoweredOIDCImplicitFlowThirdPartySSO.pdf).

After configuring the realm, you must configure this repo's code to be able to speak to the realm. These are the variables you will need:
* `TOZID_REALM_NAME` - the name of your realm
* `TOZID_CLIENT_ID` - the client_id of the client you created in the TozID realm
* `TOZID_HOSTNAME` - the location of the TozID instance, most likely `https://id.tozny.com`
* `TOZID_ROLE_NAME` - the name of the role that controls whether or not you see the big red button!

Note that with the Implicit flow the **client_secret** is not required.

The sample will automatically set the **redirect_uri** to the host
location that the sample is running on. You need to make sure that
this matches what you specified as the Redirect Uri when you
setup your OIDC app connector in the TozId Realm Admin portal.

### Running as local server

Set your configuration directly in the [config.js](public/javascripts/config.js).

Run the server with:
```
npm start
```

Your application will be running at `http://localhost:3000`.

You will need to add your callback url (e.g. `http://localhost:3000`) to the list of approved **Redirect URIs** for your OIDC client application via the TozID Realm Admin portal the client application is located in.

### Building & hosting externally

This application can also be compiled into pure HTML/CSS/JS for hosting externally.

In this case, the configuration comes from environment variables. See the example env required for building.

After your [`.env`](example.env)) is setup, run the build command (if you haven't run `npm install` previously you will need to do so now):


```bash
npm run build
```

Your ready-for-deployment files will be located in `build/`.

These files should then be uploaded to the s3 bucket `tozny-pam-client-demo` (your upload will essentially be a "new deployment" and overwrite the previous version) in the New Dev AWS account (ID: 518519311314)

Once uploaded you can then use the the deployed application by opening your browser to the [s3 hosted "website" for the bucket](http://tozny-pam-client-demo.s3-website-us-west-2.amazonaws.com)
