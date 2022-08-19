from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class TokenManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(user__icontains=query) | \
            models.Q(token__icontains=query)
        )


class Token(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    token = models.CharField(_('Token'), max_length=100)
    quantity = models.DecimalField(_('Quantity'), decimal_places=6, max_digits=8)
    purchase_price = models.DecimalField(_('Purchase_price'), decimal_places=2, max_digits=8)
    purchased_at = models.DateTimeField(_('Purchased_at'), editable=True, auto_now_add=False)
    sale_price = models.DecimalField(_('Sale_price'), decimal_places=2, max_digits=8, blank=True, null=True)
    sold_at = models.DateTimeField(_('Sold_at'), editable=True, auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField(_('Is_active'), default=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)
    # created_by = models.ForeignKey(User, verbose_name=_("Created by"), related_name="token_created_by", editable=False, on_delete=models.CASCADE)
    # updated_by = models.ForeignKey(User, verbose_name=_('Updated by'), related_name="token_updated_by", editable=False, on_delete=models.CASCADE)

    objects = TokenManager()

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'
        ordering = ['token']

    def __str__(self):
        """
        String for representing the token object (in Admin site etc.)
        """
        return str(self.user)
