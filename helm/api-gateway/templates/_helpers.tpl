{{- define "api-gateway.fullname" -}}
{{ include "api-gateway.name" . }}-{{ .Release.Name }}
{{- end }}

{{- define "api-gateway.name" -}}
api-gateway
{{- end }}

{{- define "api-gateway.labels" -}}
app.kubernetes.io/name: {{ include "api-gateway.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}