# Urheberrechtsschutz + Restricted Access

## Allgemeine Informationen

Das LibRML kann aus den folgenden Werten abgeleitet werden:

- [Access Status](https://wiki.dnb.de/pages/viewpage.action?pageId=217533654) = [Restricted Access](http://purl.org/coar/access_right/c_16ec)
- [Rechtehinweis](https://wiki.dnb.de/pages/viewpage.action?pageId=217533656) = [Urheberrechtsschutz 1.0](http://rightsstatements.org/vocab/InC/1.0/)

Hinweis:

- Es wird eine Bereitstellung des Objekts entsprechend [Bereitstellung digitaler Dokumente, die dem Urheberrecht unterliegen](https://wiki.dnb.de/pages/viewpage.action?pageId=212780202) beschrieben.
- Es wird keine Garantie für die juristische Korrektheit gegeben.

```xml
<?xml encoding="ASCII" version="1.0"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
    <item copyright="true" id="copyright-ra-100" template="LibRML Copyright - Restricted Access" tenant="https://www.slub-dresden.de/" usageguide="http://librml.org/examples/copyright_restrictedaccess">
        <action permission="true" type="displaymetadata"/>
        <action permission="true" type="index"/>
        <action permission="true" type="read">
          <restriction inside="library" type="location"/>
        </action>
        <action permission="true" type="archive"/>
    </item>
</libRML>
```

```json
{
  "id": "copyright-ra-100",
  "tenant": "https://www.slub-dresden.de/",
  "usageguide": "https://librml.org/examples/copyright_restrictedaccess",
  "template": "LibRML Copyright - Restricted Access",
  "copyright": true,
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
      "type": "archive",
      "permission": true
    }
  ]
}
```
