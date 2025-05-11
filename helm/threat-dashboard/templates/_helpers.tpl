{{- define "threat-dashboard.name" -}}
threat-dashboard
{{- end -}}

{{- define "threat-dashboard.fullname" -}}
{{ include "threat-dashboard.name" . }}
{{- end -}}
