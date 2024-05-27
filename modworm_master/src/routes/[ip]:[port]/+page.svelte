<script lang="ts">
  import "$lib/app.css";
  import {page} from '$app/stores';
  import {onMount} from 'svelte';

  import {VerifySlave} from '$lib/modbus_client';
  import LoadingSnake from '$lib/loadingsnake.svelte';
  import RegisterMap from './registermap.svelte';

  let verified: boolean = false;
  let verify_complete: boolean = false;
  onMount(async () => {
    verified = await VerifySlave($page.params.ip, $page.params.port);
    verify_complete = true;
  });

</script>


{#if !verify_complete}
  <LoadingSnake />
{:else}
  {#if verified}
    <RegisterMap />
  {:else}
    <div class="flex flex-col h-dvh justify-center items-center">
      <h1 class="text-3xl">unable to discover {$page.params.ip}:{$page.params.port}</h1>
      <a class="text-5xl p-6" href="/">&larr;</a>
    </div>
  {/if}
{/if}


