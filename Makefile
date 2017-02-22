VERSION = 1.0.0
ZIPNAME= python3_crawl.zip

all:
	/bin/rm -rf venv
	/usr/bin/virtualenv venv -p /usr/bin/python3.4
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	/bin/rm -rf deploy/$(ZIPNAME)
	/usr/bin/zip -r deploy/$(ZIPNAME) venv myrobot.py lambda.py --exclude=*Makefile* --exclude=*deploy*
	/usr/bin/aws s3 cp deploy/$(ZIPNAME) s3://lambdacoderepo/$(ZIPNAME)
