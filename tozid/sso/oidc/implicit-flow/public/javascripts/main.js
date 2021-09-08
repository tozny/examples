document.getElementById('login').addEventListener("click", redirectToLogin, false);

Oidc.Log.logger = console;
Oidc.Log.level = Oidc.Log.INFO;

//
// OIDC Client Configuration
//
const TOZID_REALM_NAME = 'example'
const TOZID_CLIENT_ID = 'demo';
const TOZID_HOSTNAME = 'https://id.tozny.com';

var settings = {
    authority: `${TOZID_HOSTNAME}/auth/realms/${TOZID_REALM_NAME}/.well-known/openid-configuration`,
    client_id: TOZID_CLIENT_ID,
    redirect_uri: window.location.origin,
    response_type: 'id_token token',
    scope: 'openid profile roles',
    filterProtocolClaims: true,
    loadUserInfo: true
};
var mgr = new Oidc.UserManager(settings);

//
// Redirect to TozId to authenticate the user
//
function redirectToLogin(e) {
  e.preventDefault();

  mgr.signinRedirect({state:'some data'}).then(function() {
      console.log("signinRedirect done");
  }).catch(function(err) {
      console.log(err);
  });
}

//
// Handle the authentication response returned
// by TozId after the user has attempted to authenticate
//
function processLoginResponse() {
  mgr.signinRedirectCallback().then(function(user) {
      document.getElementById("loginResult").innerHTML = '<h3>Success</h3><pre><code>' + JSON.stringify(user, null, 2) + '</code></pre>'
      maybeBuildAdminSection(user.profile)

  }).catch(function(err) {
      console.log(err);
  });
}

//
// Update the admin section if the provided profile has an "admin" role
//
function maybeBuildAdminSection(profile) {
    let roles = profile.realm_access?.roles;
    if (Array.isArray(roles) && roles.includes("admin")) {
        console.log(roles)
        document.getElementById("adminOnly").innerHTML = '<p><a class="btn big-red" id="adminButton">ADMIN ONLY</a></p>'
        document.getElementById("adminButton").addEventListener("click", popUpAlertAdmin, false);
    } else {
        console.log(profile.realm_access)
        document.getElementById("adminOnly").innerHTML = '<h3>nothing to see here</h3>'
    }
}

//
// Create an alert, to be used in callbacks
//
function popUpAlertAdmin(e) {
    e.preventDefault()
    alert("You are an admin!")

}

//
// Look out for a authentication response
// then log it and handle it
//
if (window.location.href.indexOf("#") >= 0) {
  processLoginResponse();
}
