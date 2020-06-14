# Demo app for DJDT database peformance guide

See this [blog post](https://mattsegal.dev/django-debug-toolbar-performance.html) on Django database performance for more details.

Also used for [this blog post](https://mattsegal.dev/django-factoryboy-dummy-data.html) on generating dummy test data.

Steps to get set up

```bash
# Install dependencies
pip install -r requirements.txt

# Generate test data
cd demo/
./manage.py migrate
./manage.py setup_test_data

# Run Django dev server
./manage.py runserver
```
