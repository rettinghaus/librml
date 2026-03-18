# Anzeige des Objekts

Zugang zum Objekt zur Ansicht ohne weitere Nutzungsmöglichkeiten, wie Speichern oder Drucken.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- read (Lesen)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- Keine

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="readonly-449" template="Read only" tenant="https://www.slub-dresden.de/">
    <action permission="true" type="displaymetadata"/>
    <action permission="true" type="index"/>
    <action permission="true" type="read"/>
    <action permission="true" type="archive"/>
  </item>
</libRML>
```

```json
{
  "id": "readonly-449",
  "tenant": "https://www.slub-dresden.de/",
  "template": "Read Only",
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
      "type": "read",
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    }
  ]
}
```
