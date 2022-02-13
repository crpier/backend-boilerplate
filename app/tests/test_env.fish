set -gx APP_PORT 80
set -gx SERVER_HOST http://localhost:$APP_PORT
set -gx SENTRY_DSN ""
set -gx POSTGRES_SERVER todo
set -gx POSTGRES_USER tadmin odo
set -gx POSTGRES_PASSWORD todo
set -gx POSTGRES_DB todo
set -gx SQLALCHEMY_DATABASE_URI 'postgresql://todo:todo@todo'
set -gx FIRST_SUPERUSER todo@example.com
set -gx FIRST_SUPERUSER_PASSWORD todo
