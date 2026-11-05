# Junta os models em um lugar só.
# Fica separado para o Migrate enxergar as tabelas
# com um único "from app import models" no create_app().

from app.models.usuario import Usuario