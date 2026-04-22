variable "aws_region" {
  description = "Region de AWS"
  type        = string
  default     = "us-east-1"
}
variable "project_name" {
  description = "Nombre base del proyecto"
  type        = string
  default     = "lab-iac-web"
}
variable "db_name" {
  description = "Nombre de la base de datos"
  type        = string
  default     = "appdb"
}
variable "db_username" {
  description = "Usuario administrador de MySQL"
  type        = string
  default     = "admin"
}
variable "db_password" {
  description = "Password administrador de MySQL"
  type        = string
  sensitive   = true
}