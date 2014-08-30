# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


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


def send_mail(**kwargs):
    try:
        item = kwargs["instance"]
    except Exception:
        return

    for participant in item.participants.all():
        if participant.email:
            data = (
                item.subject,
                datetime.strftime(item.date, "%d/%m/%Y"),
                item.time
            )

            message_text = "Evento: %s\nDia: %s\nHora: %s\n" % data
            message_text += "\nDetalhes:\n%s" % item.description
            participant.email_user(
                subject="[Evento] %s dia %s as %s" % data,
                message=message_text,
                from_email=item.user.email
            )


models.signals.post_save.connect(
    send_mail,
    sender=schedule_item,
    dispatch_uid="agenda.models.ItemAgenda"
)
