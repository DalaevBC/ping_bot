from django.db import models


class Task(models.Model):
    username = models.CharField(verbose_name='Имя сотрудника', max_length=30)
    task_name = models.CharField(verbose_name='Текст задачи', max_length=100)
    per_day = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество напоминаний за 1 день'
    )

    def time_dates(self):
        quantity = 24 / self.per_day
        time_list = [0, ]  # [0, 6, 12, 18]
        for num in range(self.per_day - 1):
            new_time = time_list[num] + quantity
            time_list.append(new_time)
        return time_list





