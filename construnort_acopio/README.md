# Manual Técnico - construnort_acopio

**Módulo**: `construnort_acopio` | **Versión**: 15.0.1.0.0 | **Odoo**: 15.0 | **Fecha**: 16/12/2025

---

## 1. Instalación y Configuración Inicial

### Requisitos
- **Odoo**: 15.0 | **Python**: 3.8+
- **Dependencias**: `['sale']`

### Instalación
1. Copiar el módulo a la carpeta de addons de Odoo: `/opt/odoo/addons/construnort_acopio` o similar.
2. Reiniciar Odoo y actualizar la lista de aplicaciones.
3. Instalar el módulo desde el backend de Odoo.
4. Asignar el grupo `Acopio - Permiso` a los usuarios que deban operar el flujo.

---

## 2. Arquitectura del Módulo

```
construnort_acopio/
├── __manifest__.py
├── __init__.py
├── models/
│   └── sale_order.py
├── wizard/
│   └── sale_order_acopio_wizard.py
├── views/
│   ├── sale_order_views.xml
│   └── sale_order_acopio_wizard_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── security_groups.xml
```

- **Extiende**: `sale.order` (agrega estado `acopio` y método para abrir wizard)
- **Wizard**: `sale.order.acopio.wizard` (confirma cambio de estado)
- **Permisos**: Grupo `Acopio - Permiso` (controla acceso al botón y wizard)

---

## 3. Configuración y Permisos

- No requiere credenciales ni endpoints externos.
- Solo usuarios con el grupo `Acopio - Permiso` pueden ver el botón y ejecutar el wizard.
- Permisos definidos en `security/ir.model.access.csv` y `security/security_groups.xml`.

---

## 4. Lógica de Negocio y Flujo

1. Usuario con grupo adecuado abre un pedido de venta.
2. Si el pedido no está en estado `acopio`, ve el botón "Acopio".
3. Al presionar el botón, se abre un wizard de confirmación.
4. Si el usuario marca el booleano y confirma, el pedido pasa a estado `acopio`.
5. El statusbar de la vista se actualiza mostrando el nuevo estado.

**Diagrama de flujo:**
```
[Pedido de venta abierto]
	│
	▼
¿Usuario tiene grupo "Acopio - Permiso"?
	│
	├─ No → No ve el botón
	│
	└─ Sí
	     │
	     ▼
¿Pedido ya en estado acopio?
	│
	├─ Sí → Botón oculto
	│
	└─ No
	     │
	     ▼
[Botón "Acopio"] → [Wizard] → [Confirmar] → [Cambia a estado acopio]
```

---

## 5. Estados y Códigos

| Código    | Descripción | Uso en el módulo         |
|-----------|-------------|--------------------------|
| draft     | Borrador    | Nativo Odoo              |
| sent      | Cotización enviada | Nativo Odoo      |
| sale      | Pedido confirmado | Nativo Odoo        |
| acopio    | Acopio      | **Agregado por el módulo** |
| done      | Cerrado     | Nativo Odoo              |
| cancel    | Cancelado   | Nativo Odoo              |

---

## 6. Troubleshooting Técnico

- **El botón "Acopio" no aparece**: Verificar grupo de usuario y estado del pedido.
- **No se puede instalar el módulo**: Verificar dependencia `sale` y permisos en `ir.model.access.csv`.
- **El wizard no cambia el estado**: Marcar el booleano y revisar permisos de acceso al wizard.

---

## 7. Comandos Útiles

```bash
# Actualizar el módulo
./odoo-bin -u construnort_acopio -d <nombre_db>

# Ver logs de Odoo
tail -f /var/log/odoo/odoo-server.log
```

---

**Notas**: Este módulo es 100% interno a Odoo, no integra sistemas externos ni algoritmos complejos. La clave técnica es la correcta asignación de permisos y la extensión limpia del flujo de estados de `sale.order`.
