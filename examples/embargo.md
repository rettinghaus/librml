# Embargofrist

Aufgrund eines Embargos ist der Zugang zum Digitalisat bis zum 31. Dezember 2028 nur eingeschränkt, d.h. in verminderter Auflösung, möglich.

Ab dem 1. Januar 2029 ist der Zugang dann uneingeschränkt möglich.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Ausdrucken)
- print (Herunterladen)

**Art der Einschränkung**:

- quality (Auflösung) mit date (zeitlich)

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="false" id="embargo-28" template="IP" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="archive"/>
    <action permission="true" type="read">
      <restriction maxresolution="72" type="quality"/>
      <restriction todate="2028-12-31" type="date"/>
    </action>
    <action permission="true" type="read">
      <restriction fromdate="2029-01-01" type="date"/>
    </action>
    <action permission="true" type="download">
      <restriction maxresolution="72" type="quality"/>
      <restriction todate="2028-12-31" type="date"/>
    </action>
    <action permission="true" type="download">
      <restriction fromdate="2029-01-01" type="date"/>
    </action>
    <action permission="true" type="print">
      <restriction maxresolution="72" type="quality"/>
      <restriction todate="2028-12-31" type="date"/>
    </action>
    <action permission="true" type="print">
      <restriction fromdate="2029-01-01" type="date"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "embargo-28",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": false,
  "template": "IP",
  "actions": [
    {
      "type": "displaymetadata",
      "permission": true
    },
    {
      "type": "index",
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    }
  ]
}
```
