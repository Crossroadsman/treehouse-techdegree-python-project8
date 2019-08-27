from .models import Mineral


group_list = Mineral.objects.order_by().values_list('group', flat=True).distinct()
group_match = 'exact'

category_list = ['Amphibole', 'Antimonide', 'Arsenate', 'Arsenic', 'Arsenide', 'Arsenite', 'Borate', 'Carbonate', 'Chromate', 'Copper', 'Dark mica', 'Feldspar', 'Feldspathoid', 'Garnet', 'Halide', 'Inosilicate', 'Iodate', 'Manganese', 'Metals and intermetallic alloys', 'Meteorite', 'Molybdate', 'Native', 'Nesosilicates', 'Nitrate', 'Organic', 'Oxalate', 'Oxide', 'Phosphate', 'Pyroxene', 'Rare earth', 'Selenate', 'Selenide', 'Silicate', 'Sulfate', 'Sulfide', 'Sulfosalt', 'Tectosilicates', 'Tektoborate', 'Telluride', 'Tellurate', 'Tellurite', 'Titanium', 'Tungstate', 'Uranium', 'Vanadate', 'Zeolite']
category_match = 'contains'

strunz_classification_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09'] # use start with
strunz_classification_match = 'startswith'

formula_list = ['Ag', 'Al', 'As', 'Au', 'B', 'Ba', 'Be', 'Bi', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cl', 'Co', 'Cr', 'Cs', 'Cu', 'F', 'Fe', 'Ge', 'H', 'Hg', 'I', 'K', 'La', 'Li', 'Mg', 'Mn', 'Mo', 'N', 'Na', 'Nb', 'Nd', 'Ni', 'O', 'P', 'Pb', 'Pd', 'Pt', 'Rb', 'Re', 'REE', 'S', 'Sb', 'Sc', 'Se', 'Si', 'Sn', 'Sr', 'Ta', 'Te', 'Th', 'Ti', 'Tl', 'U', 'V', 'W', 'Y', 'Zn', 'Zr']
formula_match = 'regex'
formula_regex_before = r''
formula_regex_after = r'([^a-z]|$)'

crystal_system_list = ['Amorphous', 'Coexisting phases', 'Cubic', 'Dipyramidal', 'Ditrigonal', 'Hexagonal', 'Hexoctahedral', 'Isometric', 'Monoclinic', 'Orthorhombic', 'Pinacoidal', 'Prismatic', 'Pyramidal', 'Rhombohedral', 'Scalenohedral', 'Tetragonal', 'Triclinic', 'Trigonal']
crystal_system_match = 'icontains'


class GroupLookup:
    """Constructs an object that can generate querysets from:
    - name: the name of the model field (e.g., `strunz_classification`)
    - list: a list of valid values
    - match: the type of match (using django's syntax)
    - (optional: used for regex mode only) before: a raw string to be prefixed 
      before the lookup value
    - (optional: used for regex mode only) after: a raw string to be appended
      to the lookup value

    Examples:
    
    1. Group
    ```
    > group = GroupLookup('group', group_list, 'exact')
    > group.get_matching_queryset(1)
    ```
    Constructs a queryset using a filter that looks like:
    Mineral.objects.filter(group__exact='Arsenates')

    2. Category
    ```
    > group = GroupLookup('category', category_list, 'contains')
    > group.get_matching_queryset(3)
    ```
    Constructs a queryset using a filter that looks like:
    Mineral.objects.filter(category__contains='Arsenic')

    3. Formula
    ```
    > group = GroupLookup('formula', formula_list, 'regex', before=r'', after=r'[^a-z]')
    > group.get_matching_queryset(4)
    ```
    Constructs a queryset using a filter that looks like:
    Mineral.objects.filter(formula__regex=r'B([^a-z]|$)')

    Note this regex will match:
    - B<sub>2</sub>Na;
    - Be<sub>3</sub>B
    - BBe
    - B
    but not
    - Be
    """

    def __init__(self, name, list, match, before=None, after=None):
        self.name = name
        self.list = list
        self.match = match
        self.before = before
        self.after = after
    
    def make_pattern(self, i):
        if self.before == None or self.after == None:
            raise ValueError('To use regex both `before` and `after` must have valid values')
        return self.before + self.list[i] + self.after
    
    def make_key_and_value(self, i):
        
        if self.match == 'regex':
            value = self.make_pattern(i)
        else:
            value = self.list[i]
        key = self.name + "__" + self.match
        return {key: value}

    def get_matching_queryset(self, i):
        filter_kwarg = self.make_key_and_value(i)
        matches = Mineral.objects.filter(**filter_kwarg)
        return matches
    
    def __str__(self):
        return self.name


groups = {
    'group': GroupLookup(name='group', list=group_list, match=group_match),
    'category': GroupLookup(name='category', list=category_list, match=category_match),
    'strunz classification': GroupLookup(name='strunz_classification', list=strunz_classification_list, match=strunz_classification_match),
    'formula': GroupLookup(name='formula', list=formula_list, match=formula_match, before=formula_regex_before, after=formula_regex_after),
    'crystal system': GroupLookup(name='crystal_system', list=crystal_system_list, match=crystal_system_match),
}
