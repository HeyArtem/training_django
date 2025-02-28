from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name="Текст")
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
        verbose_name="Тест",
    )
    image = models.ImageField(
        upload_to="questions/image/%Y/%m/%d", verbose_name="Картинка"
    )

    position = models.PositiveIntegerField(
        default=1, null=False, blank=False, verbose_name="Позиция в тесте"
    )

    def __str__(self):
        return self.text

    class Meta:
        db_table = "questions"
        # unique_together = ["test", "position"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросов"
