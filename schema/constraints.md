# Constraints - Einschränkungen

## Allgemeine Informationen

Einschränkungen (`constraints`) spezifizieren die Zugangs- und Nutzungsbeschränkungen der Nutzungsarten (`action`).
Die Einschränkungen gelten ausdrücklich nur für die `action`, der sie zugewiesen sind. Einschränkungen, die für mehrere Nutzungsarten gelten, müssen jeder `action` zugewiesen werden.

Einschränkungen können durch [Attributes (Eigenschaften)](attributes.md) weiter spezifiziert werden.

```xml
  <action permission="true" type="ACTION-NAME">
    <restriction ATTRIBUT-NAME="WERT" type="CONSTRAINT-NAME"/>
  </action>
```

```json
  "actions": [{
    "type": "ACTION-NAME",
    "permission": true,
    "restrictions": [{
        "type": "CONSTRAINT-NAME",
        "ATTRIBUT-NAME": "WERT"
     }]
  }]
```

## Liste

In LibRML stehen folgende Einschränkungen zur Verfügung.

| Constraint-Name | Übersetzung | Beschreibung | Beispiel |
| :-------------- | :--------- | :---------- |:------- |
| age | Alter | Einschränkung auf Nutzer eines bestimmten Alters. | [→&nbsp;Age](#age) |
| agreement | Einwilligung | Einschränkung hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | [→&nbsp;Agreement](#agreement) |
| concurrent | gleichzeitig | Einschränkung auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, o. Ä. | [→&nbsp;Concurrent](#concurrent) |
| count | Anzahl | Einschränkung auf eine bestimmte Anzahl an Ausführungen, Benutzungen, o. Ä. | [→&nbsp;Count](#count) |
| date | Zeitpunkt | Einschränkung ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | [→&nbsp;Date](#date) |
| duration | Dauer | Einschränkung auf eine bestimmte Zeitdauer. | [→&nbsp;Duration](#duration) |
| group | Gruppe | Einschränkung auf bestimmte Personen oder Personengruppen. | [→&nbsp;Group](#group) |
| location | Ort | Einschränkung auf ein bestimmtes Gebiet (z. B. `Deutschland`)oder auf eine bestimmte Einrichtung (z. B. `SLUB`). | [→&nbsp;Location](#location) |
| parts | Teile | Einschränkung auf bestimmte Teile des digitalen Objekts. | [→&nbsp;Parts](#parts) |
| quality | Qualität | Einschränkung auf eine maximale Qualität. | [→&nbsp;Quality](#quality) |
| watermark | Wasserzeichen | Einschränkung auf eine Kennzeichnung des digitalen Objekts mit einem Wasserzeichen oder einer anderen Markierung. | [→&nbsp;Watermark](#watermark) |

## Beispiele

### Parts

```xml
  <action permission="true" type="download">
    <restriction parts="1" type="parts"/>
  </action>
```

```json
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "parts",
      "parts": "1"
    },
```

### Group

```xml
  <action permission="true" type="print">
    <restriction groups="registered employee" type="group"/>
  </action>
```

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "group",
      "groups": [
        "registered",
        "employee",
      ]
    },
```

### Age

```xml
  <action permission="true" type="read">
    <restriction suminagebnet="18" type="age"/>
  </action>
```

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "age",
      "minage": "18"
    },
```

### Location

```xml
  <action permission="true" type="download">
    <restriction inside="library" type="location"/>
  </action>
```

```json
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "location",
      "inside": "library"
    },
```

### Date

```xml
  <action permission="true" type="distribute">
    <restriction fromdate="2035-01-01" type="date"/>
  </action>
```

```json
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "date",
      "fromdate": "2035-01-01"
    },
```

### Duration

```xml
  <action permission="true" type="run">
    <restriction duration="86400" type="duration"/>
  </action>
```

```json
  "type": "run",
  "permission": true,
  "restrictions": [
    {
      "type": "duration",
      "duration": 86400
    },
```

### Count

```xml
  <action permission="true" type="print">
    <restriction count="10" type="count"/>
  </action>
```

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "count",
      "count": 10
    },
```

### Concurrent

```xml
  <action permission="true" type="lend">
    <restriction sessions="4" type="concurrent"/>
  </action>
```

```json
  "type": "lend",
  "permission": true,
  "restrictions": [
    {
      "type": "concurrent",
      "sessions": 4
    },
```

### Watermark

```xml
  <action permission="true" type="distribute">
    <restriction type="watermark" watermarkvalue="https://domain/watermark.png"/>
  </action>
```

```json
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "watermark",
      "watermarkvalue": "https://domain/watermark.png"
    },
```

### Quality

```xml
  <action permission="true" type="print">
    <restriction maxresolution="300" type="quality"/>
  </action>
```

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "quality",
      "maxresolution": 300
    },
```

### Agreement

```xml
  <action permission="true" type="read">
    <restriction required="true" type="agreement"/>
  </action>
```

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "agreement",
      "required": true
    },
```
