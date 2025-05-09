{{- define "detector.name" -}}
detector
{{- end -}}

{{- define "detector.fullname" -}}
{{ include "detector.name" . }}
{{- end -}}
