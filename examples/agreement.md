# Einwilligung

Zugang und Nutzung nur nach Einwilligung, zum Beispiel durch Abschluss eines Nutzungsvertrags oder Bestätigung von Nutzungsbestimmungen.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)
- reproduce (Vervielfältigen)
- modify (Bearbeiten)
- reuse (Wiederverwenden)
- distribute ((Ver)teilen)
- publish (Veröffentlichen oder vorführen)
- move (Übertragen der Daten)

**Art der Einschränkung**:

- agreement (Einwilligung)

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="true" id="agreement-DE-447" template="Agreement" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="archive"/>
    <action permission="true" type="read">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="download">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="print">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="reproduce">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="modify">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="reuse">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="distribute">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="publish">
      <restriction required="true" type="agreement"/>
    </action>
    <action permission="true" type="move">
      <restriction required="true" type="agreement"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "agreement-DE-447",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": true,
  "template": "Agreement",
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
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "reproduce",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "modify",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "reuse",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "distribute",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "publish",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "move",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    }
  ]
}
```
