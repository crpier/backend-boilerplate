/usr/bin/env fish

set -gx APP_PORT "80"
set -gx SERVER_HOST "http://localhost:$APP_PORT"
set -gx SENTRY_DSN ""
set -gx MARIADB_SERVER "127.0.0.1:3306"
set -gx MARIADB_USER "root"
set -gx MARIADB_PASSWORD "super"
set -gx MARIADB_DB "app"
set -gx SQLALCHEMY_DATABASE_URI "mariadb+pymysql://root:super@127.0.0.1:3306/app"
set -gx FIRST_SUPERUSER "todo@example.com"
set -gx FIRST_SUPERUSER_PASSWORD "todo"
