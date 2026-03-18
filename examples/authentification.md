# Authentifizierung

Zugang und Nutzung nur nach Authentifizierung. In LibRML wird dies durch Zugehörigkeit zu einer Gruppe beschrieben.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)

**Art der Einschränkung**:

- group (Gruppe)

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="true" id="auth-DE-442" template="Authentification" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="archive"/>
    <action permission="true" type="read">
      <restriction groups="registered" type="group"/>
    </action>
    <action permission="true" type="download">
      <restriction groups="registered" type="group"/>
    </action>
    <action permission="true" type="print">
      <restriction groups="registered" type="group"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "auth-DE-442",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": true,
  "template": "Authentification",
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
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    }
  ]
}
```
