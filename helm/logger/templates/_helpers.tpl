{{- define "logger.name" -}}
logger
{{- end -}}

{{- define "logger.fullname" -}}
{{ include "logger.name" . }}
{{- end -}}