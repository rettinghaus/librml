Übersicht der Beispiele hinsichtlich [Anpassung LibRML für Retrodigitalisate](adjustments.md).

# Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht

Diese LibRML-Beispiele reflektieren die Rechte- und Nutzungshinweise, die unter <https://nutzungshinweis.slub-dresden.de/ez-am-ua/1.0/> zusammengefasst sind.

## Beispiel A: aktuelles LibRML

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="LibRML">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-ua/1.0/">
                        <libRML:action permission="true" type="displaymetadata"/>
                        <libRML:action permission="false" type="download"/>
                        <libRML:action permission="true" type="index"/>
                        <libRML:action permission="false" type="publish"/>
                        <libRML:action permission="true" type="read">
                            <libRML:restriction sessions="1" type="concurrent"/>
                            <libRML:restriction inside="SLUB-PC-Arbeitsplätze-Lesesaal(Sammlungen)" type="location"/>
                            <libRML:restriction required="true" type="agreement"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel B: angepasstes LibRML

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="LibRML">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-ua/1.0/">
                        <libRML:action permission="true" type="displaymetadata">
                            <libRML:restriction sections="amdSec dmdSec structMap" type="mets"/>
                        </libRML:action>
                        <libRML:action permission="false" type="download"/>
                        <libRML:action permission="true" type="index">
                            <libRML:restriction sections="dmdSec" type="mets"/>
                        </libRML:action>
                        <libRML:action permission="true" type="publish">
                            <libRML:restriction OAI-PMH="internal" type="interface"/>
                        </libRML:action>
                        <libRML:action permission="true" type="read">
                            <libRML:restriction sessions="1" type="concurrent"/>
                            <libRML:restriction inside="SLUB-PC-Arbeitsplätze-Lesesaal(Sammlungen)" type="location"/>
                            <libRML:restriction filegroups="AUDIO DEFAULT VIDEO" type="mets"/>
                            <libRML:restriction details="Unter Aufsicht" type="agreement"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```
