# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User


class schedule_item(models.Model):
    schedule_item_id = models.IntegerField(
        "Código",
        max_length=11,
        primary_key=True
    )

    date = models.DateField("Data")
    time = models.TimeField("Hora")
    subject = models.CharField("Assunto", max_length=100)
    description = models.TextField("Descrição", null=True)
    user = models.ForeignKey(User)
    participants = models.ManyToManyField(User,
                                          related_name="schedule_participants")

    class Meta:
        db_table = "schedule_items"
        permissions = (("can_list_item", "Pode listar itens"))
        unique_together = (("subject", "date", "time"))
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ["date", "time"]

    def __unicode__(self):
        return "{0} em {1} as {2}".format(self.subject, self.date, self.time)


class schedule_participant(models.Model):

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
