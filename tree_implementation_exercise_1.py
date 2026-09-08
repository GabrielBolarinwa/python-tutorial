class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, *args):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if "designation" in args:
            print(f"{prefix} {self.designation}")
        elif "name" in args:
            print(f"{prefix}{self.name}")
        else:
            print(f"{prefix}{self.name} ({self.designation})")
        if self.children:
            for child in self.children:
                child.print_tree(*args)


def build_employee_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    infra = TreeNode("Vishwa", "Infrastructure Head")
    infra.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(infra)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)
    return root


if __name__ == "__main__":
    employee_tree = build_employee_tree()
    employee_tree.print_tree()
    employee_tree.print_tree("name")
    employee_tree.print_tree("designation")
