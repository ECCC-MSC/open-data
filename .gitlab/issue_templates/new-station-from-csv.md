Convert **inster CSV file** into GeoJSON.

Steps:

* Make sure the CSV is encoded in UTF-8 to print correctly the French caracters
```python
import chardet
with open('input.csv', 'rb') as f:
    data = f.read()

encoding_result = chardet.detect(data)
encoding = encoding_result['encoding']
print("Detected Encoding:", encoding)
```
* If encoding is not UTF-8 (ex: Windows-1252): 
  * `iconv -f Windows-1252 -t UTF8 swob-xml_partner_station_list.csv > output.csv`
* Convert the CSV to a GeoJSON using a ogr2ogr command
  * `ogr2ogr -f "GeoJSON" output.geojson output.csv -oo X_POSSIBLE_NAMES=Longitude -oo Y_POSSIBLE_NAMES=Latitude`



