# Ticketera Web 🦋

### 2° Parcial - PPIII | IFTS N°18

> Desarrollo e Implementación de Sistemas en la Nube

---

## Integrantes ᨳଓ

- Lola Commenge
- Cande Ali
- Nuria Pamela Lescano

---

Aplicación web desarrollada en Python y Flask para la gestión de solicitudes de soporte técnico. La solución integra autenticación mediante Active Directory, control de acceso basado en roles y administración de tickets.

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

---

## Persistencia ᨳଓ

La información de los tickets se almacena en archivos JSON, permitiendo conservar el estado, responsables, comentarios e historial de cada solicitud.

---

## Seguridad ᨳଓ

- Autenticación mediante Active Directory (LDAP)
- Restricción horaria de acceso
- Control de acceso según rol
- Validación de entradas de usuario
