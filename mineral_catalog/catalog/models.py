from django.db import models


class Mineral(models.Model):

    # example: "Abelsonite"
    name = models.CharField(max_length=255)
    # example:
    # "240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA
    # .jpg"
    image_filename = models.CharField(max_length=255)
    # example:
    # "Abelsonite from the Green River Formation, Uintah County, Utah, US"
    image_caption = models.TextField()
    # example: "Organic"
    category = models.CharField(max_length=255)
    # example: "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni"
    formula = models.CharField(max_length=255)
    # example: "10.CA.20"
    strunz_classification = models.CharField(max_length=255)
    # example: "Triclinic"
    crystal_system = models.CharField(max_length=255)
    # example:
    # "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z =
    #  1"
    unit_cell = models.CharField(max_length=255)
    # example:
    # "Pink-purple, dark greyish purple, pale purplish red, reddish brown"
    color = models.CharField(max_length=255)
    # example: "Space group: P1 or P1Point group: 1 or 1"
    crystal_symmetry = models.CharField(max_length=255)
    # example: "Probable on {111}"
    cleavage = models.CharField(max_length=255)
    # example: "2–3"
    mohs_scale_hardness = models.CharField(max_length=255)
    # example: "Adamantine, sub-metallic"
    luster = models.CharField(max_length=255)
    # example: "Pink"
    streak = models.CharField(max_length=255)
    # example: "Semitransparent"
    diaphaneity = models.CharField(max_length=255)
    # example: "Biaxial"
    optical_properties = models.CharField(max_length=255)
    # example: "Organic Minerals"
    group = models.CharField(max_length=255)

    # example: "nω = 1.597 – 1.608nε = 1.570"
    refractive_index = models.CharField(max_length=255,
                                        blank=True,
                                        default="")
    # example:
    # "Tabular to pyramidal crystals, also fibrous, lamellar, earthy, massive
    #  granular"
    crystal_habit = models.CharField(max_length=255,
                                     blank=True,
                                     default="")
    # example: "3.95 - 3.97"
    specific_gravity = models.CharField(max_length=255,
                                        blank=True,
                                        default="")

    class Meta:
        # make first character in string a `-` to reverse order
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def fieldnames_and_values(self):
        """Provides a convenient dictionary where all the keys are the fields
        and the values are the fields with spaces separating the words"""
        fields = self._meta.get_fields()

        data = {}
        for field in fields:
            data[field.name] = {
                'name': field.name.replace("_", " "),
                'value': getattr(self, field.name)
            }
        return data
