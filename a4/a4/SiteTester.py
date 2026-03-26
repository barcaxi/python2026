from Site import Site

site = Site('N14 Letterkenny IT', '54.952089', '-7.7208929')
print(site.get_site_name())
site.set_site_name('N14 ATU Letterkenny')
print(site.get_site_name())

print(site.get_lat())
print(site.get_lng())

print(site.to_string())
print(site.to_dict())
