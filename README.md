OpenShift-CherryPy
---

This is an example that show how to use [CherryPy](http://cherrypy.org/) with [OpenShift](https://www.openshift.com/) and the [mod_wsgi](http://modwsgi.readthedocs.org/en/latest/) components.

To use this examle create a Python Application following the 
[online examples](https://www.openshift.com/get-started/) or with:

```
rhc create-app -a cherrypy -t python-2.7
```
Following this you can pull in the code from these examples by using:

```
git remote add quickstart https://github.com/penguinforge/openshift-cherrypy.git
git fetch quickstart
git checkout master; git merge --strategy=recursive -X theirs quickstart/master
git push
```

This example works like most other WSGI applicaion examples by [defining CherryPy as a dependency](https://github.com/penguinforge/openshift-cherrypy/blob/master/setup.py#L9)
and then defining the [mod_wsgi application](https://github.com/penguinforge/openshift-cherrypy/blob/master/wsgi/application#L19)

The OpenShift `python` cartridge documentation can be [found here](https://github.com/openshift/origin-server/tree/master/cartridges/openshift-origin-cartridge-python/README.md).

Credit: The magic of this example is provided by [tools.cherrypy](http://tools.cherrypy.org/wiki/ModWSGI)
