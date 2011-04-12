# Create your views here.


from eve_db import models
from django.http import HttpResponse
from django.template import loader, Context

def ascsystems(request):
	a = models.map.MapSolarSystem.objects.all()
	c = []
	e = float('1e16')
	for b in a:
		d = {
		'x1': b.x_min/e,
		'y1': b.y_min/e,
		'z1': b.z_min/e,
		'x2': b.x_max/e,
		'y2': b.y_max/e,
		'z2': b.z_max/e,
		'r' : 255,
		'g' : 0,
		'b' : 0
		}
		c.append(d)

	response = HttpResponse(mimetype='text/plain')
	response['Content-Disposition'] = 'attachment; filename=systems.asc'

	t = loader.get_template('pointcloud.asc')
	c = Context({
	    'systems': c,
	})
	response.write(t.render(c))
	return response

