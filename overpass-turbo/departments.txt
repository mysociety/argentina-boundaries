[out:json];

area["name"="Argentina"];
(
  relation
  ["boundary"="administrative"]
  ["admin_level"=5](area);
);

out body;
>;
out skel qt;