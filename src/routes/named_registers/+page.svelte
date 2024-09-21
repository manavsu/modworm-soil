<script lang="ts">
    import Title from '$lib/title.svelte';
    import { fade } from 'svelte/transition';
    import { NamedRegisters } from "$lib/store";
    import { NamedRegisterDataType, modbus_data_type_to_named_register_data_type} from "./named_register_data_type";
    import { data_type_to_int } from "$lib/modbus_data_type";
    import { CurrentTable, ConnectedSocket, SelectedDataType } from "$lib/store";
    import { ReadRegisters } from "$lib/modbus_client";
    import {function_code} from "$lib/modbus_table";

    let named_registers;
    let read_error = null;

	async function read_named_registers() {
        read_error = null;
        if ($CurrentTable == null || $ConnectedSocket == null){
            named_registers = [];
            return;
        }
		try {
            for (let i = 0; i < $NamedRegisters.length; i++) {
                
			    const result = await ReadRegisters($ConnectedSocket.address, $ConnectedSocket.port, function_code($CurrentTable.type), $CurrentTable.register_list[i][1], data_type_to_int($SelectedDataType));
            }
			register_groups = [...register_groups];
		} catch (error) {
			read_error = error;
		}
	}

    $: named_registers = $NamedRegisters.map(register => {
        return {
            name: "register_" + register.address,
            address: register.address,
            value: register.value,
            type: modbus_data_type_to_named_register_data_type(register.type)
        }
    });
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full w-full overflow-auto scrollbar-thin">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
        <div class="flex flex-col justify-center h-14">
            <Title>Named Registers</Title>
        </div>
    </div>

    {#each $NamedRegisters as register, i}
        <div>{register.address} {register.type} {register.value}</div>    
    {/each }
</div>
