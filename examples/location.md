# IP-Adressbereich

Zugang und Nutzung nur innerhalb eines IP-Adressbereichs, wie zum Beispiel Campusnetz.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Ausdrucken)
- print (Herunterladen)

**Art der Einschränkung**:

- location (ortsspezifisch)

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="false" id="iprestricted-444" template="IP" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="archive"/>
    <action permission="true" type="read">
      <restriction subnet="192.168.10.0/24" type="location"/>
    </action>
    <action permission="true" type="download">
      <restriction subnet="192.168.10.0/24" type="location"/>
    </action>
    <action permission="true" type="print">
      <restriction subnet="192.168.10.0/24" type="location"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "iprestricted-444",
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
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    }
  ]
}
```
