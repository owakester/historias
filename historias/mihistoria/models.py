from django.db import models
class MyModelName(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-field_name"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.field_name