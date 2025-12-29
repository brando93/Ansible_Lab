# Apache Role

Este role instala y configura Apache2 en servidores Linux.

## Descripción

El role `apache_role` automatiza la instalación de Apache2, despliega una página HTML personalizada y asegura que el servicio esté corriendo y habilitado.

## Requisitos

- Sistema operativo: Ubuntu/Debian (con paquete apache2)
- Privilegios: Se requiere `become: true` para instalar paquetes y gestionar servicios

## Variables del Role

Las siguientes variables están definidas en `vars/main.yml`:

- `nombre`: Nombre a mostrar en la página web (default: "Brandon")
- `apellido`: Apellido a mostrar en la página web (default: "Rodriguez")

## Estructura del Role

```
roles/apache_role/
├── defaults/main.yml      # Variables por defecto (pueden ser sobrescritas)
├── vars/main.yml          # Variables del role (alta prioridad)
├── tasks/main.yml         # Tareas principales del role
├── handlers/main.yml      # Handlers para reiniciar Apache
├── templates/             # Templates Jinja2
│   └── index.html.j2      # Página HTML personalizada
└── files/                 # Archivos estáticos (si se necesitan)
```

## Uso

### Opción 1: Usar el playbook incluido

Desde el directorio `ansible/`:

```bash
ansible-playbook -i inventory playbooks/deploy_apache.yml
```

### Opción 2: Incluir el role en tu propio playbook

Crea un playbook en `playbooks/`:

```yaml
---
- name: Deploy Apache
  hosts: webservers
  become: true
  roles:
    - apache_role
```

Luego ejecútalo:

```bash
ansible-playbook -i inventory playbooks/tu_playbook.yml
```

### Opción 3: Sobrescribir variables

```yaml
---
- name: Deploy Apache with custom variables
  hosts: webservers
  become: true
  roles:
    - role: apache_role
      vars:
        nombre: "Juan"
        apellido: "Pérez"
```

## Estructura de Directorios Ansible

```
ansible/
├── inventory              # Inventario de hosts
├── playbooks/            # Playbooks que usan roles
│   └── deploy_apache.yml
└── roles/                # Directorio de roles
    └── apache_role/      # Este role
        ├── defaults/
        ├── vars/
        ├── tasks/
        ├── handlers/
        └── templates/
```

## Tareas que realiza el role

1. **Instalar Apache2**: Instala el paquete apache2 usando el gestor de paquetes del sistema
2. **Desplegar index.html**: Copia el template personalizado a `/var/www/html/index.html`
3. **Iniciar Apache2**: Asegura que el servicio esté corriendo y habilitado en el arranque
4. **Handler**: Reinicia Apache2 cuando se detectan cambios en la configuración

## Handlers

- `Restart apache2`: Reinicia el servicio Apache2 cuando se modifica el archivo index.html

## Ejemplo de salida

Después de ejecutar el role, la página web mostrará:

```html
<h1>Hello Brandon Rodriguez</h1>
```

## Diferencias con el playbook original

Este role es una conversión del playbook `apache/apache.yml` con las siguientes mejoras:

- ✅ Estructura modular siguiendo las mejores prácticas de Ansible
- ✅ Separación de variables, tareas y handlers
- ✅ Template en el directorio correcto (`templates/` en lugar de `files/`)
- ✅ Handler para reiniciar Apache cuando hay cambios
- ✅ Reutilizable en múltiples playbooks
- ✅ Fácil de mantener y extender
- ✅ Ubicado en `roles/` siguiendo la estructura estándar de Ansible

## Licencia

MIT-0
