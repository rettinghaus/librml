# Agreement
## 3. Zugang nur nach Abschluss eines Nutzungsvertrags

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive | Nutzungsvertrag | read<br/><br/>download<br/><br/>print<br/><br/>reproduce<br/><br/>modify<br/><br/>reuse<br/><br/>distribute<br/><br/>publish<br/><br/>move |

**JSON**
{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "template": "Only Metadata Access",
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
    },
  ]
}

{% endhighlight %}


**XML**
{% highlight xml %}
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.3">
  <item id="doi:10.1371/journal.pbio.0020447" tenant="http://slub-dresden.de" template="Authentification">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="download" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="print" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="reproduce" permission="true">
      <restriction type="agreement" required="true"/>
    </action> 
    <action type="modify" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="reuse" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="distribute" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="publish" permission="true">
      <restriction type="agreement" required="true"/>
    </action>
    <action type="move" permission="true">
      <restriction type="agreement" required="true"/>
    </action>    
  </item>
</libRML>
{% endhighlight %}