# Gleichzeitiger Zugriff

Zugang und Nutzung ist auf eine bestimmte Menge gleichzeitiger Zugriffe beschränkt.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)

**Art der Einschränkung**:

- concurrent (Gleichzeitig)

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="true" id="concuracc-440" template="ConcurrentAccess" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="archive"/>
    <action permission="true" type="read">
      <restriction sessions="5" type="concurrent"/>
    </action>
    <action permission="true" type="download">
      <restriction sessions="5" type="concurrent"/>
    </action>
    <action permission="true" type="print">
      <restriction sessions="5" type="concurrent"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "concuracc-440",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": true,
  "template": "ConcurrentAccess",
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
          "type": "concurrent",
          "sessions": 5
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    }
  ]
}
```
