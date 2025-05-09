{{- define "llm-proxy.name" -}}
llm-proxy
{{- end -}}

{{- define "llm-proxy.fullname" -}}
{{ include "llm-proxy.name" . }}
{{- end -}}
