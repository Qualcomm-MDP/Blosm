"use client"
import { Environment, OrbitControls } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import { Model } from "./Model"

export function MainCanvas() {

    return(
        <div className="w-screen h-screen fixed top-0 left-0">
            <Canvas
                shadows
                dpr={[1, 2]}
                camera={{fov: 55, position: [0, 500, 35]}}
            >
                <Environment files="/images/ashphalt.jpg"></Environment>
                <Model position={[0, 0, 0]}/>

                <OrbitControls />
            </Canvas>
        </div>
    );
}