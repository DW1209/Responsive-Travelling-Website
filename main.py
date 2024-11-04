import os
from website import create_app


app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 19019))
    app.run(host='0.0.0.0', port=port)
