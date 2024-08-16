{{- define "common.labels" -}}
app: "{{ .Chart.Name }}"
appVersion: "{{ .Chart.AppVersion }}"
version: "{{ .Chart.Version }}"
release: "{{ .Release.Name }}"
revision: "{{ .Release.Revision }}"
{{- end -}}
