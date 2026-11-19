# Ticketera Web 🦋

### 2° Parcial - PPIII | IFTS N°18

> Desarrollo e Implementación de Sistemas en la Nube

---

## Integrantes ᨳଓ

- Lola Commenge
- Cande Ali
- Nuria Lescano

---

Aplicación web desarrollada en Python y Flask para la gestión de solicitudes de soporte técnico. La solución integra autenticación mediante Active Directory, control de acceso basado en roles y administración de tickets.

---
## Entrgable ᨳଓ

https://docs.google.com/document/d/1hZ6pC4GRabzkYgKElUHovOC7U16JtJyX0riqo7aip6Y/edit?usp=sharing

---

## Funcionalidades ᨳଓ

Autenticación mediante Active Directory (LDAP)
<br>
Restricción horaria de acceso
<br>
Gestión de roles y permisos
<br>
Creación de tickets
<br>
Consulta y actualización de tickets
<br>
Gestión de estados (Abierto, En Progreso, Resuelto y Cerrado)
<br>
Asignación de prioridades y responsables
<br>
Comentarios de seguimiento
<br>
Historial de cambios
<br>
Persistencia de datos en formato JSON
<br>
Exportación de información en formato CSV

---

## Roles ᨳଓ

### Admin
Acceso completo al sistema.

### Operador
Gestión y actualización de tickets.

### Usuario
Creación y consulta de solicitudes.

### Consulta
Acceso de solo lectura.

---

## Active Directory ᨳଓ

Se implementó un dominio Active Directory para la autenticación de usuarios y la asignación de permisos mediante grupos.

### Usuarios

- admin
- juan
- pedro
- maria

### Grupos

- Admin
- Operador
- Usuario
- Consulta

---

## Tecnologías utilizadas ᨳଓ

Python | Flask | HTML | CSS | JSON | CSV | Active Directory | LDAP | VirtualBox

La aplicación Ticketera Web es un sistema de gestión de soporte técnico desarrollado en Python bajo el microframework Flask, encargado de gestionar el enrutamiento web, las sesiones de usuario, la validación de permisos mediante decoradores y el renderizado dinámico de las plantillas HTML estilizadas con CSS. El entorno de pruebas se desplegó de manera aislada utilizando VirtualBox para virtualizar tanto el servidor de dominio como los clientes de prueba.

Para la seguridad y el control de acceso, la aplicación se integra con Active Directory mediante el protocolo LDAP, autenticando las credenciales directamente contra el controlador de dominio. Una vez validado el usuario, el sistema aplica una restricción de acceso por franja horaria y asigna los privilegios correspondientes según los perfiles definidos (Admin, Operador, Usuario y Consulta). Por último, la persistencia de las solicitudes , que incluye título, descripción, prioridad, estado (Abierto, En Progreso, Resuelto, Cerrado), responsable, comentarios e historial de cambios, se almacena en formato JSON, mientras que la exportación de reportes descargables se genera dinámicamente en formato CSV.


---

## Persistencia ᨳଓ

La información de los tickets se almacena en archivos JSON, permitiendo conservar el estado, responsables, comentarios e historial de cada solicitud.

---

## Seguridad ᨳଓ

- Autenticación mediante Active Directory (LDAP)
- Restricción horaria de acceso
- Control de acceso según rol
- Validación de entradas de usuario
