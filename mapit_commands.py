from mapit.models import Area, Generation

argentina = Area.objects.get(pk=958805)

generation = Generation.objects.current()

provinces = list(Area.objects.intersect('coveredby', argentina, ['O04'], generation))
departments = list(Area.objects.intersect('coveredby', argentina, ['O05'], generation))

province_ids = [p.id for p in provinces]
department_ids = [d.id for d in departments]
