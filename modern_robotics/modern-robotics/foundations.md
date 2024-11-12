# Foundations of Robot Motion

## Configuration Space (C-Space)

Robots are mechanically constructed by connecting a set of bodies called **links** to each other using various types of **joints**. Powered by **Acutators** the robot's link move which are usually attached to an **end-effector**, such as a gripper or hand for grasping and manipulating objects. We'll focus on links that are modeled as rigid bodies.

Robots are defined by their **configuration** - the specification of the position of all points of the robot. Since robot's links are rigid and have a known shape, we only need to represent the configuration as a few numbers, known as **degrees of freedom (dof)**. 

### Degrees of Freedom (dof)

Robots typically have 6 dof, $[x, y, z]$ for position (linear) and $[roll, pitch, yaw]$ for movement (angular).

We compute the dof using the following formula:

$$
\text{dof} = \sum{(\text{freedoms of points}) - \text{number of independent constraints}}
$$

The constraints on motion often come from the **joints**. 

We can simplify our dof formula using the following:

$$
\text{dof} = m(N - 1) - \sum_{i=1}^{J} c_i
$$

Where:
- $N$ = number of bodies (links), including ground (body that doesn't move).
- $J$ = number of joints.
- $m$ = 6 for spatial bodies (3D space), 3 for planar (2D space).
- $c_i$ = number of joint constraints for joint $i$ (can differ for $m$).
- Number of links, ignoring ground: $N - 1$.
- Rigid body freedoms without joint constraints: $m(N - 1)$.
- All joint constraints:

$$
\sum_{i=1}^{J} c_i
$$

- Single joint constraint $c_i = (m - f_i)$. Where $f_i$ is the number of dofs provided by joint $i$. 
  
**Grübler's formula** (all constraints must be independent):

$$
\text{dof} = m(N - 1 - J) + \sum_{i=1}^{J} f_i
$$

### Joints

Joints typically have two spatial rigid bodies. The joint itself is the what allows angular movement. Common joints:

- **Revolute (R)**: 5 spatial constraints, 2 planar constraints, 1 dof. 
- **Prismatic (P)**: 5 spatial constraints, 2 planar constraints, 1 dof. Linear joint. 
- **Helical (H)**: 5 spatial constraints, 1 dof.
- **Universal (U)**: 4 spatial constraints, 2 dof.
- **Cylindrical (C)**: 4 spatial constraints, 2 dof.
- **Spherical (S)**: 3 spatial constraints, 3 dof. Ball-and-socket.

Examples:

$$
\text{dof} = m(N - 1 - J) + \sum_{i=1}^{J} f_i
$$

1. 3R serial "open-chain" robot - planar, 4 links, 3R joints.

$$
dof = 3(4 - 1 - 3) + 3 = 3
$$

2. Four-bar "closed-chain" mechanism - planar, 4 links, 4R joints.

$$
dof = 3(4 - 1 - 4) + 4 = 1
$$

3. Stewart platform 6xUPS - spatial, 14 links (6 UPS legs + ground + top platform), 18 joints (3 per leg).

$$
dof = 6(14 - 1 - 18) + 36 = 6
$$

### Topology

Another important property is the shape of the space. For example, the space of a plane and a sphere are very different.

Two spaces are **topologically equivalent** if one can be smoothly deformed to the other without cutting and gluing.

In one-dimensional space we have 3 common distinct topologies: a circle, a line, and a closed interval of a line.

In two-dimensional space we have: a plane, the surface of a sphere, the surface of a torus, and the surface of a cylinder.

| System           | Topology               | Configuration Representation    |
|------------------|------------------------|---------------------------------|
| Point on a plane | Plane (2D euclidean space -> $\mathbb{E}^2$) | $\dot{(x, y)}$ -> (2 real numbers -> $\mathbb{R}^2$) |
| Spherical pendulum | Sphere (2D surface -> $S^2$) | (latitude, longitude) -> $[-180^{\circ}, 180^{\circ}) \cdot [-90^{\circ}, 90^{\circ}]$ |
|2R robot arm | Torus ($T^2 = S^1 \cdot S^1$) | 2 coordinates -> $[0, 2\pi) \cdot [0, 2\pi)$ |
| Rotating sliding knob | Cylinder ($\mathbb{E^1} \cdot S^1$) | (sliding distance, angle) -> $\mathbb{R}^1 \cdot [0, 2\pi)$ |

The configuration representation for each system and topology is arbitrary, we define it ourselves. 

Focusing on our 2R robot arm example, we can get the space of coordinates by cutting the torus once to get a **cylinder** and then again to get a square subet of the **plane**. 
