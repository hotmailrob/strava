Pour avoir le bon access token, il faut appeler l'uri de auth avec le refresh_toke. 
Par exemple, le refresh token donné directement par strava n'est que pour read le profiile. 

Pour avoir un refresh token avec un autre scope, il faut aller sur un url , qui spécifi le scope, et ensuite noter le code dans l'uri de la page de redirect après avoir approve. 
https://www.strava.com/oauth/authorize?client_id=103301&response_type=code&redirect_uri=http://localhost/exchange_token&scope=activity:read,activity:write

Ensuite, on peut appeler  : auth_url = "https://www.strava.com/oauth/token" en donnant le code pris dans le dernier URL (du redirect) et recevoir un nouveau refresh token avec les bons accès ! 
